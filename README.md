<!--
README.md file intended to outline scope of the projects being
worked on as well as to serve as a changelog... for now.
-->

<a id="readme-top"></a>

# TK.Main

Welcome to **TK.Main**!

This Github repository serves as a working directory to organize and co-develop various tools to improve comprehension of development, cyber security, networking, cloud, and project management.

---
<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

### **February 13th, 2025 – Peach and Wizard**
- Added the [**TK.snapandlearn**](/Projects/TK.snapandlearn/) project.
  - Project is currently in MVP state.
- Added [Projects](/Projects/) folder to provide better structure for projects.
- Created and linked a kanban board (project management board): [TK.Board](https://github.com/users/JustKeagsTheWizard/projects/2).

---
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🛠️ Setup Instructions

If you're invited to this project, here's how to get started:

1. **Set Up WSL and VS Code**:
   - Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) on your Windows machine.
   - Install [VS Code](https://code.visualstudio.com/) and [configure](https://code.visualstudio.com/blogs/2019/09/03/wsl2) it to work with WSL.

2. **Connect GitHub via SSH**:
   - Generate an SSH key using the command:
     ```sh
     ssh-keygen -t ed25519 -C "your_email@example.com"
     ```
   - Add the key to your SSH agent:
     ```sh
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     ```
    - If you receive the `Permissions for '/root/.ssh/id_ed25519/' are too open` error: run the following command to correct the permissions for the file.
      ```sh
      chmod 600 ~/.ssh/id_ed25519
      ```
   - Copy the SSH key to your clipboard:
     ```sh
     cat ~/.ssh/id_ed25519
     ```
   - Add the SSH key to your [GitHub](https://github.com/settings/keys) account under **Settings > SSH and GPG keys**.

3. **Optional: Sign Commits with GPG**:
   - Generate a GPG key if you don’t have one:
     ```sh
     gpg --full-generate-key
     ```
   - Add the GPG key to your [GitHub](https://github.com/settings/keys) account under **Settings > SSH and GPG keys**.
   - Configure Git to use the GPG key:
     ```sh
     git config --global user.signingkey YOUR_GPG_KEY_ID
     git config --global commit.gpgsign true
     ```

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Goals

- Build something cool and innovative.
- Learn from failures and iterate.
- Document the journey for future reference.
- Create a Streamlit web application that incorporates OAuth2.0

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing

If you'd like to contribute to this project, feel free to:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is closed-source and not available to the general public.

---
<p align="right">(<a href="#readme-top">back to top</a>)</p>