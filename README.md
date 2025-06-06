# 🏴 Scavenger Flag Concatenator

A simple but handy Python script to **concatenate split flags** found in CTF challenges like `Scavenger Hunt` from [picoCTF](https://picoctf.org).

---

## 🔧 Why I Created This

In challenges like `Scavenger Hunt`, flags are often split into multiple parts and hidden across different files — such as HTML comments, JavaScript, or other hidden files like `.htaccess`.

I got tired of copying and pasting each part manually just to reconstruct the final flag.  
So I wrote this tool to make my life easier — and maybe yours too 

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python concat_flag.py
   ```

2. When prompted, enter each part of the flag:
   ```
   Insert first flag: picoCTF{
   Insert second flag: scavenger_
   Insert third flag: hunt_
   Insert fourth flag: is_
   Insert fifth flag: fun}
   ```

3. Output:
   ```
   <-----SEPARATED FLAG----->
   first flag: picoCTF{
   second flag: scavenger_
   third flag: hunt_
   fourth flag: is_
   fifth flag: fun}

   <-----CONCATED FLAG----->
   picoCTF{scavenger_hunt_is_fun}
   ```

---

## 🛠 Features

- Takes exactly max 10 parts of the flag
- Prints each part clearly
- Joins all parts into a single flag string

---

## 📚 About This Script

This was made during my time solving CTFs, especially [picoCTF](https://picoctf.org).  
The goal was **not just to solve flags faster**, but also to automate small tasks that get annoying after a while.

Feel free to fork, star, or suggest improvements.

---

## 👤 Author

Made with frustration (and love) by KyzaaDev
