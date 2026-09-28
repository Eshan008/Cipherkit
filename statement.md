# Statement

## Problem Statement

Most people learning cryptography only see classical ciphers as pen-and-paper exercises or isolated command-line scripts. There is no single, easy-to-use tool that lets a learner experiment interactively with multiple classical ciphers, see immediate results, and review a history of past operations, all without needing to touch a terminal.

**Goal:** Build a self-contained desktop application that allows a user to select a classical cipher, supply a key, and encrypt or decrypt arbitrary text, while keeping a persistent, reviewable history of every operation performed.

## Scope of the Project

- Support four classical ciphers: Caesar, Vigenère, Rail Fence, and Substitution.
- Provide a single-window GUI with a cipher workspace and a history viewer.
- Validate keys and inputs per cipher, with clear error feedback.
- Persist every encrypt/decrypt operation to a local JSON history file.
- Allow the user to clear history and copy output to the clipboard.

**Out of scope:** modern or asymmetric cryptography (e.g. AES, RSA), networked or multi-user features, and cloud storage of history. The tool is intentionally local, offline, and focused on classical ciphers.

## Target Users

Students and self-learners studying introductory cryptography or information security concepts, who want a hands-on tool to encrypt and decrypt text and understand how classical ciphers transform data.

## High-Level Features

1. **Cipher selection and key input:** choose a cipher from a dropdown, with a live hint showing the expected key format.
2. **Encryption and decryption:** a common `encrypt(text, key)` / `decrypt(text, key)` interface implemented by each cipher module and registered in a single `CIPHERS` dictionary, so new ciphers can be added without touching the GUI.
3. **Validation and error handling:** non-empty input checks and per-cipher key validation, shown as clear dialog messages instead of crashes.
4. **History and logging:** every operation is timestamped and saved; the History tab lists past operations, shows full input and output on selection, and lets the user clear the history.
