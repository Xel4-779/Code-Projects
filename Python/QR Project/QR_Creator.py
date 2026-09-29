"""A small desktop app for creating QR code images.

Install dependency with: python -m pip install qrcode[pil]
"""

import tkinter as tk
from tkinter import filedialog, messagebox

import qrcode


def create_qr():
    data = entry.get("1.0", "end-1c").strip()

    if not data:
        messagebox.showwarning("Missing content", "Enter text or a URL first.")
        return

    filename = filedialog.asksaveasfilename(
        title="Save QR code",
        defaultextension=".png",
        initialfile="qr_code.png",
        filetypes=[("PNG image", "*.png"), ("All files", "*.*")],
    )
    if not filename:
        return

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white").save(filename)
    except (OSError, ValueError) as error:
        messagebox.showerror("QR code error", str(error))
        return

    messagebox.showinfo("QR code created", f"Saved QR code to:\n{filename}")


root = tk.Tk()
root.title("QR Code Creator")
root.resizable(False, False)

tk.Label(root, text="Enter text or a URL:").pack(anchor="w", padx=12, pady=(12, 4))
entry = tk.Text(root, width=48, height=7, wrap="word")
entry.pack(padx=12)
tk.Button(root, text="Create QR Code", command=create_qr).pack(pady=12)

root.mainloop()