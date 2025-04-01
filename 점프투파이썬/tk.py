import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var_operation.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("오류", "잘못된 연산 선택입니다.")
            return
        
        label_result.config(text=f"결과: {result}")
    
    except ValueError:
        messagebox.showerror("오류", "올바른 숫자를 입력해주세요.")

# GUI 설정
root = tk.Tk()
root.title("계산기")

# 숫자 입력
label_num1 = tk.Label(root, text="첫 번째 숫자:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="두 번째 숫자:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# 연산 선택
var_operation = tk.StringVar(value='+')
label_operation = tk.Label(root, text="연산:")
label_operation.grid(row=2, column=0)

option_add = tk.Radiobutton(root, text="+", variable=var_operation, value='+')
option_subtract = tk.Radiobutton(root, text="-", variable=var_operation, value='-')
option_multiply = tk.Radiobutton(root, text="*", variable=var_operation, value='*')
option_divide = tk.Radiobutton(root, text="/", variable=var_operation, value='/')

option_add.grid(row=2, column=1, sticky='w')
option_subtract.grid(row=3, column=1, sticky='w')
option_multiply.grid(row=4, column=1, sticky='w')
option_divide.grid(row=5, column=1, sticky='w')

# 계산 버튼
button_calculate = tk.Button(root, text="계산", command=calculate)
button_calculate.grid(row=6, columnspan=2)

# 결과 표시
label_result = tk.Label(root, text="결과: ")
label_result.grid(row=7, columnspan=2)

# GUI 실행
root.mainloop()