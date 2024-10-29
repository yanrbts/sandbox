# Makefile to compile all .c files in the current directory into sandbox executable

# 编译器
CC = gcc

# 编译选项
CFLAGS = -Wall -g

# 目标程序名
TARGET = sandbox

# 查找所有 .c 文件和 .h 文件
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

# 目标规则
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ)

# 自动生成 .o 文件规则
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# 清理目标
clean:
	rm -f $(OBJ) $(TARGET)

# 伪目标（不生成文件）
.PHONY: clean
