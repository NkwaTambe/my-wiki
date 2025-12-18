# A Guide to Shell Prompt Customization

This document provides a general guide to understanding and customizing your shell prompt in popular shells like Bash and Zsh.

## Core Concepts

Understanding a few core concepts is key to customizing your prompt effectively.

### What is a Shell Prompt?

The shell prompt is the text or symbols that appear in your terminal, indicating that the shell is ready to accept commands. It can be customized to display useful information, making your command-line experience more efficient and enjoyable.

### The `PS1` Variable

The primary mechanism for prompt customization in both Bash and Zsh is an environment variable called `PS1`. By changing the value of this variable, you change the appearance of your prompt.

### Shell Frameworks (The Easy Way)

For those who want a powerful, pre-configured shell experience without manual setup, frameworks are an excellent option.

-   **Oh My Zsh** is a popular framework for Zsh that comes with a vast collection of themes and plugins.
-   **Themes** are scripts that automatically set your `PS1` and other variables to a specific style. This is the easiest way to get a great-looking prompt.
-   **Plugins** add new features, commands, and aliases to your shell, extending its functionality beyond the basics.

### How Frameworks and Themes Work

Frameworks like **Oh My Zsh** simplify prompt customization by managing themes and plugins. Here's a general breakdown of the process:

1.  **The Framework**: A framework is installed and loaded when the shell starts.

2.  **The Theme**: In your shell's configuration file (e.g., `.zshrc`), you select a theme by name. This tells the framework which theme file to load.

3.  **The `PS1` Variable**: The theme file is a script that programmatically builds the `PS1` string. It handles all the complex code for colors, Git status, directory information, and other dynamic elements. This means you don't have to write a complicated `PS1` variable yourself.

4.  **Plugins**: Frameworks also manage plugins that add extra functionality, such as command syntax highlighting or autocompletion. While these don't typically alter the prompt's appearance, they work alongside it to enhance the shell experience.

In summary, the **framework** manages a **theme**, and the theme automatically sets the **`PS1`** variable to create the visual prompt. **Plugins** run alongside to add features.

## Manual Prompt Customization

For those who prefer not to use a framework, you can customize your prompt by directly setting the `PS1` variable. This section provides examples for both Zsh and Bash.

### For Bash Users

Bash uses backslash-escaped characters to represent special information in the `PS1` variable.

-   **Minimal Prompt**: `PS1='\w > '`
    -   `\w` displays the current working directory.
-   **User and Host**: `PS1='\u@\h \w > '`
    -   `\u` displays the username.
    -   `\h` displays the hostname.
-   **Adding Colors**: `PS1='\[\e[0;32m\]\u@\h \w > \[\e[0m\]'`
    -   `\[\e[0;32m\]` sets the color to green.
    -   `\[\e[0m\]` resets the color.

### For Zsh Users

Zsh uses percent-escaped characters, which offer more advanced features than Bash.

-   **Minimal Prompt**: `PS1='%~ > '`
    -   `%~` displays the current directory, with `~` for the home directory.
-   **User and Host**: `PS1='%n@%m %~ > '`
    -   `%n` displays the username.
    -   `%m` displays the hostname.
-   **Adding Colors**: `PS1='%F{green}%n@%m %~ > %f'`
    -   `%F{green}` sets the text color to green.
    -   `%f` resets the color.

### Making Changes Permanent

To make your prompt customizations permanent, you need to add the `PS1` definition to your shell's configuration file. This is the manual process that themes automate for you.

-   **For Zsh**: Add the `PS1="..."` line to the end of your `~/.zshrc` file.
-   **For Bash**: Add the `PS1="..."` line to the end of your `~/.bashrc` file.

After editing the file, you need to either open a new terminal or run `source ~/.zshrc` (for Zsh) or `source ~/.bashrc` (for Bash) for the changes to take effect.

## References

For more in-depth information, you can refer to the official documentation for each shell:

-   **Zsh**: [Zsh Manual - Prompt Expansion](http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html)
-   **Bash**: [Bash Manual - Controlling the Prompt](https://www.gnu.org/software/bash/manual/html_node/Controlling-the-Prompt.html)
