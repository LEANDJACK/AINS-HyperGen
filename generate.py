from openai import OpenAI
from pynput.keyboard import Controller, Key
import time
from tkinter import messagebox

content_english = "Without any uneeded words, get straight to the point, try to mimic a robot that follows instrucutions without any excessive actions, give the direct answer without extra words such as 'name of book' or 'book name', only writing the answers AND without the numberings BUT in different lines each, without paragraph spacing, generate the answers in the same order as the questions, help me generate a book with the following features;1. Name of book 2. Category (either fiction or non-ficton, all UPPERCASE) 3. book pages 4. ISBN number 5. Writer 6. Publisher of the book 7. Year published (after year 2000) 8. Language (ENGLISH) 9. Content of the book in around 30 words 10. Value or moral learned from this book(more than 5 words) 11. Rating given from 1-5, without decimals"
content_malay = "dengan menggunakan tema yang baru dan tidak berulang tentang pelajar kolej, tidak berkata banyak, HANYA tuliskan jawapan dengan tiada point-point TETAPI di barisan yang berbeza, tidak memakai paragraph spacing, minta tolong generatekan satu buku dengan ciri-ciri tersebut: 1. Nama buku 2.Kategori(fiksyen atau tidak fiksyen, SEMUA HURUF BESAR) 3.bilangan mukasurat 4.nombor isbn 5.penulis 6.Penerbit 7.Tahun terbitan(selepas tahun 2000) 8.Bahasa(MELAYU) 9. Rumusan buku dalam 30 patah perkataan 10.Pengajaran dalam bahasa mudah dan melebihi 5 patah perkataan 11.Rating buku(daripada 1-5, tanpa perpeluhan)"

def run_generator(language, api_key):

    # Select correct prompt
    if language == "English":
        prompt = content_english
    elif language == "Malay":
        prompt = content_malay
    else:
        raise ValueError("Unsupported language")

    # Initialize OpenAI client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
        )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    # Save to file
    with open("output.txt", "w") as f:
        f.write(output)

    # Read lines for keyboard typing
    with open("output.txt", "r") as f:
        lines = f.read().splitlines()

    (name, ficton_true, pages, isbn, author,
        publisher, year_published, language,
        book_context, moral, star) = lines[:11]

    keyboard = Controller()

    time.sleep(1)

    #typing NAME OF BOOK
    keyboard.type(name)

    # Press TAB 2 times
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #choose FICTON? (not needed)
    if ficton_true.strip().upper() == "FICTION":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    else:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


    # Press ENTER 2 times
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)

    #Type pages
    keyboard.type(pages)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #Type isbn
    keyboard.type(isbn)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #type author
    keyboard.type(author)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #type publisher
    keyboard.type(publisher)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #type year published
    keyboard.type(year_published)

    # Press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    
    #fill in the language
    if language.strip().upper() == "MELAYU":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif language.strip().upper() == "ENGLISH":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    
        

    # Press TAB 2 times
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #Press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    #rest before the storm xd
    time.sleep(1)

    # press TAB 15 times (xd)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.1)
    
    #type book context
    keyboard.type(book_context)

    #press TAB
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #type moral
    keyboard.type(moral)

    #stars statement
    if star.strip() == "1":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif star.strip() == "2":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif star.strip() == "3":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif star.strip() == "4":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif star.strip() == "5":
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.05)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
    #press tab 2 times
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.05)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #prss enter to go the the next page
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    #prss enter to go the the next page
    time.sleep(0.25)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    #press tab
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    #press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    messagebox.showinfo("Info", "Operation Completed.")
        