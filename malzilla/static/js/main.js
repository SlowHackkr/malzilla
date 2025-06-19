// Malzilla JS (Optional Enhancements)
// This file can enhance UX such as showing filename or previewing upload.

document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.querySelector('input[type="file"]');
    const fileLabel = document.createElement("p");

    fileLabel.style.color = "#94a3b8";
    fileLabel.style.marginTop = "0.5rem";

    fileInput.parentElement.appendChild(fileLabel);

    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
            fileLabel.textContent = `Selected file: ${fileInput.files[0].name}`;
        } else {
            fileLabel.textContent = "";
        }
    });
});
