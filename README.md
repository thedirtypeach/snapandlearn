<!--
Keagan, I deleted the original text you had here.

This website kicks ass for testing out how your "readme.md" file
will look: [stackedit.io](https://stackedit.io/app#)

It's designed for testing markdown... which Streamlit supports!
-->

# TK.Main

Welcome to **TK.Main**! This repository marks the beginning of an exciting journey to build something amazing—or fail spectacularly while learning valuable lessons along the way. Either way, it's going to be a great experience!

---

## 📅 Timeline

### **February 7, 2025 – The Wizard**
- Repository created.
- Set up **WSL (Windows Subsystem for Linux)** and **VS Code**.
- Connected GitHub to the WSL instance via **SSH**.
- Configured commits to be signed with a **GPG key**.

### **February 8, 2025 – Peach**
- Initially faced some confusion while cloning the repository.
- With the help of **Deepseek**, figured out the steps to:
  1. Generate a new **SSH key**.
  2. Add the key to the **SSH agent**.
  3. Print the key to the terminal and copy it.
  4. Add the SSH key to my GitHub account for authentication.
- Learned that using **GPG to sign commits** is optional (and skipped it for now).
- Confirmed that to push/pull changes, you need:
  - A GitHub account with access to this repository (with proper permissions).
  - A corresponding SSH key for authentication.

---

## 🛠️ Setup Instructions

If you're invited to this project, here's how to get started:

1. **Set Up WSL and VS Code**:
   - Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) on your Windows machine.
   - Install [VS Code](https://code.visualstudio.com/) and [configure](https://code.visualstudio.com/blogs/2019/09/03/wsl2) it to work with WSL.

2. **Connect GitHub via SSH**:
   - Generate an SSH key using the command:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com"
     ```
   - Add the key to your SSH agent:
     ```bash
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     ```
   - Copy the SSH key to your clipboard:
     ```bash
     cat ~/.ssh/id_ed25519.pub
     ```
   - Add the SSH key to your [GitHub](https://github.com/settings/keys) account under **Settings > SSH and GPG keys**.

3. **Optional: Sign Commits with GPG**:
   - Generate a GPG key if you don’t have one:
     ```bash
     gpg --full-generate-key
     ```
   - Add the GPG key to your [GitHub](https://github.com/settings/keys) account under **Settings > SSH and GPG keys**.
   - Configure Git to use the GPG key:
     ```bash
     git config --global user.signingkey YOUR_GPG_KEY_ID
     git config --global commit.gpgsign true
     ```

---

## 🚀 Goals

- Build something cool and innovative.
- Learn from failures and iterate.
- Document the journey for future reference.
- Create a Streamlit web application that incorporates OAuth2.0

---

## 🤝 Contributing

If you'd like to contribute to this project, feel free to:
1. Fork the repository (you may have to request access from The Wizard).
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Let’s BUILD SOMETHING! 🎉🎉🎉