console.log("CodeMaster UI Loaded Successfully");
// ===============================
// DISABLE COPY-PASTE IN CODE EDITOR
// ===============================
document.addEventListener("DOMContentLoaded", function () {
    const editors = document.querySelectorAll(".no-paste");

    editors.forEach(editor => {

        // Block keyboard paste (Ctrl+V / Cmd+V)
        editor.addEventListener("paste", function (e) {
            e.preventDefault();
            alert("⚠️ Pasting code is not allowed. Please type manually.");
        });

        // Block copy (optional but recommended)
        editor.addEventListener("copy", function (e) {
            e.preventDefault();
        });

        // Block cut
        editor.addEventListener("cut", function (e) {
            e.preventDefault();
        });

        // Block drag & drop paste
        editor.addEventListener("drop", function (e) {
            e.preventDefault();
        });

        // Allow TAB indentation
        editor.addEventListener("keydown", function (e) {
            if (e.key === "Tab") {
                e.preventDefault();
                const start = this.selectionStart;
                const end = this.selectionEnd;
                this.value =
                    this.value.substring(0, start) +
                    "    " +
                    this.value.substring(end);
                this.selectionStart = this.selectionEnd = start + 4;
            }
        });
    });
});