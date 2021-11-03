from media_list import InternationalMedia
if __name__ == "__main__":
    test_file = open("test_paragraph.txt", "r")
    text = test_file.read()
    test_file.close()

    print("=== ORIGINAL TEXT ===")
    print(text)

    print("=== SEGMENTED TEXT ===")
    print(text.split("\n\n"))
