const dropzone  = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const submitBtn = document.getElementById('submitBtn');
const clearBtn  = document.getElementById('clearBtn');
const status    = document.getElementById('status');

let selectedFile = null;

function setStatus(msg, isError = false) {
  status.textContent = msg;
  status.className = 'status' + (isError ? ' error' : '');
}

function showPreview(file) {
  selectedFile = file;
  const reader = new FileReader();
  reader.onload = (e) => {
    dropzone.innerHTML = `
      <img class="preview" src="${e.target.result}" alt="preview" />
      <div class="preview-overlay">
        <span class="preview-label">✓ ${file.name}</span>
      </div>`;
    submitBtn.disabled = false;
    clearBtn.classList.add('visible');
    setStatus(`Ready — ${(file.size / 1024).toFixed(0)} KB`);
  };
  reader.readAsDataURL(file);
}

function resetDropzone() {
  selectedFile = null;
  fileInput.value = '';
  dropzone.innerHTML = `
    <div class="drop-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" stroke="var(--accent)">
        <path d="M12 16V4m0 0-3.5 3.5M12 4l3.5 3.5"/>
        <path d="M3 16v1a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3v-1"/>
      </svg>
    </div>
    <span class="drop-label">Drop your image here</span>
    <span class="drop-sub">or click to browse files</span>`;
  submitBtn.disabled = true;
  clearBtn.classList.remove('visible');
  setStatus('');
}

dropzone.addEventListener('click', () => fileInput.click());
dropzone.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') fileInput.click(); });

fileInput.addEventListener('change', () => {
  if (fileInput.files[0]) showPreview(fileInput.files[0]);
});

dropzone.addEventListener('dragover', (e) => { e.preventDefault(); dropzone.classList.add('drag-over'); });
dropzone.addEventListener('dragleave', () => dropzone.classList.remove('drag-over'));
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropzone.classList.remove('drag-over');
  const file = e.dataTransfer.files[0];
  if (!file) return;
  if (!file.type.startsWith('image/')) { setStatus('Please drop an image file.', true); return; }
  showPreview(file);
});

clearBtn.addEventListener('click', resetDropzone);

submitBtn.addEventListener('click', async () => {
  if (!selectedFile) return;
  submitBtn.disabled = true;
  setStatus('Uploading…');
  const fd = new FormData();
  fd.append('image', selectedFile);
  try {
    const res = await fetch('/upload', { method: 'POST', body: fd });
    const data = await res.json();
    if (data.success) {
      setStatus(`Found: ${data.year}`);
    } else {
      setStatus('Something went wrong.', true);
      submitBtn.disabled = false;
    }
  } catch {
    setStatus('Network error. Please try again.', true);
    submitBtn.disabled = false;
  }
});