

SUBDIR := ./exercises

clean:
	find $(SUBDIR) -type f -perm +111 -exec rm {} \;