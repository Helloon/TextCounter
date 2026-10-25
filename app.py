import tkinter as tk


def count_characters(text):
    """Return the total number of Unicode characters, including whitespace."""
    return len(text)


def create_window():
    window = tk.Tk()
    window.title("文字字数统计器")
    window.geometry("480x320")
    window.minsize(360, 240)

    input_box = tk.Text(
        window,
        height=10,
        wrap="word",
        font=("Microsoft YaHei UI", 11),
        padx=8,
        pady=8,
    )
    input_box.pack(fill="both", expand=True, padx=16, pady=(16, 10))

    result_label = tk.Label(
        window,
        text="字符总数：0",
        font=("Microsoft YaHei UI", 12),
    )
    result_label.pack(pady=(0, 8))

    def update_count():
        text = input_box.get("1.0", "end-1c")
        result_label.config(text=f"字符总数：{count_characters(text)}")

    def clear_input():
        input_box.delete("1.0", "end")
        result_label.config(text="字符总数：0")
        input_box.focus_set()

    button_frame = tk.Frame(window)
    button_frame.pack(pady=(0, 16))

    count_button = tk.Button(
        button_frame,
        text="统计字数",
        width=16,
        font=("Microsoft YaHei UI", 11),
        command=update_count,
    )
    count_button.pack(side="left", padx=(0, 8))

    clear_button = tk.Button(
        button_frame,
        text="清空",
        width=16,
        font=("Microsoft YaHei UI", 11),
        command=clear_input,
    )
    clear_button.pack(side="left", padx=(8, 0))

    input_box.focus_set()
    return window, input_box, result_label, count_button, clear_button


def main():
    window, _input_box, _result_label, _count_button, _clear_button = create_window()
    window.mainloop()


if __name__ == "__main__":
    main()
