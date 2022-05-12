if __name__ == "__main__":
        try:
                __import__("cil01").login()
        except Exception as e:
                exit(str(e))
