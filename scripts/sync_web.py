import os
import sys
import json
import subprocess
from datetime import datetime, timezone, timedelta

# Absolute Paths provided for DailyPost365 Infrastructure
GEMINI_PATH = r"C:\Users\User\AppData\Roaming\npm\gemini"
FFMPEG_PATH = r"C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin\ffmpeg.exe"

def check_env():
    """Verify essential environment variables."""
    gh_pat = os.environ.get('GH_PAT')
    if not gh_pat:
        print("WARNING: GH_PAT environment variable not found. Git operations may fail.")
    return gh_pat

def generate_seo_title(player, milestone):
    """Auto-SEO Template for 'Click-Magnet' titles."""
    templates = [
        f"UNBELIEVABLE: {player} Just Shattered {milestone}! Watch Now!",
        f"THE KING IS BACK: {player} Historic 2026 Moment Everyone is Talking About!",
        f"2026 EXCLUSIVE: {player} {milestone} Revealed - Pure Viral!"
    ]
    # Simple selection for now, could be randomized or criteria-based
    return templates[0]

def optimize_for_bridge():
    """Calculate bridge optimization for 6:00 PM UAE / 7:30 PM IST."""
    # UAE is UTC+4, IST is UTC+5.5
    now_utc = datetime.now(timezone.utc)
    uae_time = now_utc + timedelta(hours=4)
    ist_time = now_utc + timedelta(hours=5.5)
    
    print(f"Current UAE Time: {uae_time.strftime('%I:%M %p')}")
    print(f"Current IST Time: {ist_time.strftime('%I:%M %p')}")
    
    # Check if we are in the 6:00 PM UAE / 7:30 PM IST bridge window (e.g., +/- 30 mins)
    target_uae_hour = 18
    if uae_time.hour == target_uae_hour:
        print(">>> CRITICAL: 6:00 PM UAE / 7:30 PM IST Bridge Active. Optimizing Viral Metadata...")
        return True
    return False

def load_master_vault():
    """Load data from the master vault."""
    vault_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'master_vault.json')
    if os.path.exists(vault_path):
        with open(vault_path, 'r') as f:
            return json.load(f)
    return None

def sync_cricket_content():
    """Logic for syncing Cricket-related viral content with Auto-SEO."""
    print("Syncing Cricket content...")
    vault = load_master_vault()
    if not vault:
        print("ERROR: Master Vault not found.")
        return

    bridge_status = optimize_for_bridge()
    
    players = vault.get('cricket', {}).get('international', []) + vault.get('cricket', {}).get('ipl', [])
    for player_data in players:
        name = player_data.get('name')
        milestone = player_data.get('milestone_2026')
        seo_title = generate_seo_title(name, milestone)
        print(f"SEO Generated for {name}: {seo_title}")

def main():
    print("DailyPost365 - Web Sync Engine V1.1 (SEO Ready)")
    gh_pat = check_env()
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_dir = os.path.join(base_dir, 'web')
    
    if not os.path.exists(web_dir):
        print(f"ERROR: Web directory not found at {web_dir}")
        sys.exit(1)
        
    sync_cricket_content()
    # Placeholder for Crypto logic following same pattern
    
    print("Sync complete.")

if __name__ == "__main__":
    main()
