from data_generator import CSVFileGenerator, TestFileGenerator


def main():
    TestFileGenerator.generate()
    print("Test dosyası oluşturuldu!")

    CSVFileGenerator.generate()
    print("Log dosyası başarıyla CSV formatına dönüştürüldü!")


if __name__ == "__main__":
    main()