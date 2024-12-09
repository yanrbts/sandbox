# 定义变量
CC = gcc
CFLAGS = -Wall -ggdb -Wno-unused-function -I./src
SRCDIR = src
OBJDIR = obj
TARGET = sandtable

# 搜索 src 目录下的所有 .c 文件
SOURCES := $(wildcard $(SRCDIR)/*.c)
OBJECTS := $(patsubst $(SRCDIR)/%.c, $(OBJDIR)/%.o, $(SOURCES))

# 目标规则：生成可执行文件 sandtable
$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $(OBJECTS)

# 创建 obj 目录并编译 .c 文件
$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

# 创建 obj 目录
$(OBJDIR):
	mkdir -p $(OBJDIR)

# 清理编译生成的文件
.PHONY: clean
clean:
	rm -rf $(OBJDIR) $(TARGET)
