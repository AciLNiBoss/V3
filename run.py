if __name__ == "__main__":
        try:
                __import__("acil01").login()
        except Exception as e:
                exit(str(e))
