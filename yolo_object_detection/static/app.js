const $ = (s) => document.querySelector(s);
const conf = $("#conf"), iou = $("#iou");
conf.oninput = () => ($("#confOut").value = conf.value);
iou.oninput = () => ($("#iouOut").value = iou.value);

/* ---------- tabs ---------- */
document.querySelectorAll(".tab").forEach((t) => {
  t.onclick = () => {
    document.querySelectorAll(".tab").forEach((x) => x.classList.remove("active"));
    document.querySelectorAll(".view").forEach((v) => v.classList.add("hidden"));
    t.classList.add("active");
    $("#view-" + t.dataset.tab).classList.remove("hidden");
    if (t.dataset.tab === "stats") loadLog();
  };
});

/* ---------- class list ---------- */
let CLASSES = [];
fetch("/api/classes")
  .then((r) => r.json())
  .then((d) => {
    if (!d.ok) throw new Error(d.error);
    CLASSES = d.classes;
    $("#classes").innerHTML = d.classes
      .map((c) => `<option value="${c.id}">${c.name}</option>`)
      .join("");
    $("#modelStatus").textContent = `Model ready · ${d.classes.length} classes`;
  })
  .catch((e) => {
    $("#modelStatus").className = "status err";
    $("#modelStatus").textContent =
      "Model weights not loaded. First run needs internet to download yolo11n.pt — " + e.message;
  });

const selectedClasses = () =>
  [...$("#classes").selectedOptions].map((o) => +o.value);

/* ---------- upload ---------- */
const drop = $("#drop"), fileInput = $("#file"), runBtn = $("#runBtn");
let chosen = null;

drop.onclick = () => fileInput.click();
drop.ondragover = (e) => { e.preventDefault(); drop.classList.add("over"); };
drop.ondragleave = () => drop.classList.remove("over");
drop.ondrop = (e) => {
  e.preventDefault(); drop.classList.remove("over");
  setFile(e.dataTransfer.files[0]);
};
fileInput.onchange = () => setFile(fileInput.files[0]);

function setFile(f) {
  if (!f) return;
  chosen = f;
  drop.innerHTML = `<p><strong>${f.name}</strong></p><small>${(f.size / 1048576).toFixed(1)} MB — click to change</small>`;
  runBtn.disabled = false;
}

runBtn.onclick = async () => {
  if (!chosen) return;
  runBtn.disabled = true; runBtn.textContent = "Detecting…";
  const fd = new FormData();
  fd.append("file", chosen);
  fd.append("conf", conf.value);
  fd.append("iou", iou.value);
  fd.append("track", $("#track").checked);
  fd.append("classes", selectedClasses().join(","));
  try {
    const d = await (await fetch("/api/detect", { method: "POST", body: fd })).json();
    $("#uploadResult").innerHTML = d.ok ? render(d) : `<p class="status err">${d.error}</p>`;
  } catch (e) {
    $("#uploadResult").innerHTML = `<p class="status err">${e.message}</p>`;
  }
  runBtn.disabled = false; runBtn.textContent = "Run Detection";
};

function render(d) {
  if (d.kind === "image") {
    const rows = d.detections
      .map((x) => `<tr><td>${x.label}</td><td>${(x.confidence * 100).toFixed(1)}%</td><td>${x.box.join(", ")}</td></tr>`)
      .join("");
    return `<img src="/static/${d.output_image}" />
      <div class="chips">${chips(d.counts)}</div>
      <p><small>${d.total} objects · ${d.inference_ms} ms · ${d.image_size.join("×")}</small></p>
      <table><tr><th>Class</th><th>Confidence</th><th>Box (x1,y1,x2,y2)</th></tr>${rows}</table>`;
  }
  return `<video src="/static/${d.output_video}" controls></video>
    <p><small>${d.frames} frames processed in ${d.seconds}s</small></p>
    <p><small>Unique tracked objects</small></p><div class="chips">${chips(d.unique_objects)}</div>
    <p><small>Total detections</small></p><div class="chips">${chips(d.detections_per_class)}</div>`;
}

const chips = (o) =>
  Object.entries(o || {}).map(([k, v]) => `<span class="chip">${k} · ${v}</span>`).join("") ||
  '<span class="chip">none</span>';

/* ---------- live webcam ---------- */
const cam = $("#cam"), overlay = $("#overlay");
let stream = null, running = false;
const palette = ["#36d399", "#2f81f7", "#f0883e", "#db61a2", "#e3b341", "#a371f7"];

$("#camStart").onclick = async () => {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: { width: 960, height: 540 } });
  } catch (e) {
    alert("Camera access denied or unavailable: " + e.message); return;
  }
  cam.srcObject = stream;
  await cam.play();
  overlay.width = cam.videoWidth; overlay.height = cam.videoHeight;
  running = true; loop();
};

$("#camStop").onclick = () => {
  running = false;
  stream?.getTracks().forEach((t) => t.stop());
  overlay.getContext("2d").clearRect(0, 0, overlay.width, overlay.height);
};

async function loop() {
  if (!running) return;
  const c = document.createElement("canvas");
  c.width = cam.videoWidth; c.height = cam.videoHeight;
  c.getContext("2d").drawImage(cam, 0, 0);
  try {
    const d = await (await fetch("/api/detect_frame", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        image: c.toDataURL("image/jpeg", 0.7),
        conf: +conf.value,
        classes: selectedClasses(),
      }),
    })).json();
    if (d.ok) {
      draw(d.detections);
      $("#fps").textContent = d.inference_ms + " ms";
      $("#liveCounts").innerHTML = chips(d.counts);
    }
  } catch (_) {}
  requestAnimationFrame(loop);
}

function draw(dets) {
  const ctx = overlay.getContext("2d");
  ctx.clearRect(0, 0, overlay.width, overlay.height);
  ctx.lineWidth = 2; ctx.font = "16px system-ui";
  dets.forEach((d, i) => {
    const [x1, y1, x2, y2] = d.box;
    const col = palette[i % palette.length];
    ctx.strokeStyle = col; ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
    const txt = `${d.label} ${(d.confidence * 100) | 0}%`;
    ctx.fillStyle = col;
    ctx.fillRect(x1, y1 - 20, ctx.measureText(txt).width + 10, 20);
    ctx.fillStyle = "#07140f";
    ctx.fillText(txt, x1 + 5, y1 - 5);
  });
}

/* ---------- analytics ---------- */
async function loadLog() {
  const d = await (await fetch("/api/log")).json();
  $("#logSummary").textContent = `${d.rows} detections logged across all runs.`;
  const max = Math.max(1, ...Object.values(d.counts));
  $("#logChart").innerHTML = Object.entries(d.counts)
    .map(([k, v]) => `<div class="bar"><span>${k}</span><i style="width:${(v / max) * 260}px"></i><span>${v}</span></div>`)
    .join("") || "<small>No data yet — run a detection first.</small>";
}
