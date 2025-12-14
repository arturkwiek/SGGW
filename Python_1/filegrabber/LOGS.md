### W wyniku kompilacji i uruchomienia otrzymano:
```bash
PS C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber> poetry lock
Resolving dependencies... (0.1s)

Writing lock file
PS C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber> poetry install
Installing dependencies from lock file

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2025.10.5)
  - Installing charset-normalizer (3.4.4)
  - Installing idna (3.11)
  - Installing urllib3 (2.5.0)
  - Installing requests (2.32.5)

Installing the current project: filegrabber (0.1.0)
PS C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber> poetry run grab
✅ Zapisano plik: C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber\sample.csv
⏳ Start funkcji transform ...
✅ Zakończono transform (czas: 0.054 s)
📂 Zapisano values.csv i missing_values.csv
PS C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber> poetry run python -m filegrabber.main
✅ Zapisano plik: C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber\sample.csv
⏳ Start funkcji transform ...
✅ Zakończono transform (czas: 0.018 s)
📂 Zapisano values.csv i missing_values.csv
PS C:\Users\Dell\Desktop\Workplace\Repositories\SGGW\Python_1\filegrabber> 
```