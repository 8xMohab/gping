# **gping** - My Own Improved Ping Command

This is **my version of the ping command** with a simpler, cleaner output. It streams the results live and shows the **min**, **avg**, and **max** latency when you stop it with `Ctrl+C`.

### How to Install:

#### For Linux:
1. Make sure you have **Python 3** installed.
2. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/gping.git
   ```

3. Change to the repo directory:

   ```bash
   cd gping
   ```

4. Make it executable:

   ```bash
   chmod +x gping.py
   ```

5. Optionally, move it to a directory in your `PATH` for easy access:

   ```bash
   mv gping.py ~/.local/bin/gping
   ```

6. Run it:

   ```bash
   ./gping.py
   ```

   By default, it pings **google.com**. To specify a different host, just add it like so:

   ```bash
   ./gping.py github.com
   ```

#### For Windows:
1. Install **Python 3** from [python.org](https://www.python.org/downloads/).
2. Clone the repo:

   ```powershell
   git clone https://github.com/yourusername/gping.git
   ```

3. Navigate to the repo directory:

   ```powershell
   cd gping
   ```

4. Run the script:

   ```powershell
   python gping.py
   ```

   By default, it pings **google.com**. To specify a different host, just add it like so:

   ```powershell
   python gping.py github.com
   ```

---

### Enjoy!

Feel free to use it, and let me know if you need any improvements! 

