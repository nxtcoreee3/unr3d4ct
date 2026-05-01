import cv2
import numpy as np
import os
import sys
import subprocess
import shutil

def clean_exports():
    folder = "unr3d4ct_exports"
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"[!] Cleaned up {folder}")
    else:
        print("[-] Nothing to clean.")

def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"[-] Error: Could not open {image_path}")
        return

    output_dir = "unr3d4ct_exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.basename(image_path).split('.')[0]
    
    alphas = [1.5, 3.0, 4.5]  
    betas = [-50, 0, 50]
    gammas = [0.4, 1.0, 1.8]

    total = len(alphas) * len(betas) * len(gammas)
    count = 0

    for a in alphas:
        for b in betas:
            adjusted = cv2.convertScaleAbs(img, alpha=a, beta=b)
            for g in gammas:
                inv_g = 1.0 / g
                table = np.array([((i / 255.0) ** inv_g) * 255 for i in np.arange(0, 256)]).astype("uint8")
                final = cv2.LUT(adjusted, table)
                
                out_file = f"{output_dir}/{base_name}_a{a}_b{b}_g{g}.jpg"
                cv2.imwrite(out_file, final)
                count += 1
                sys.stdout.write(f"\r[*] Processing {base_name}: {count}/{total}")
                sys.stdout.flush()

def run_dropzone():
    zone = "drop_zone"
    if not os.path.exists(zone):
        os.makedirs(zone)
        print(f"[+] Created '{zone}' folder. Drop images there and run again.")
        return

    files = [f for f in os.listdir(zone) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        print(f"[-] No images found in {zone}")
        return

    for f in files:
        process_image(os.path.join(zone, f))
    
    print(f"\n[!] Finished processing {len(files)} images.")
    subprocess.run(["open", "unr3d4ct_exports"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 unr3d4ct.py <path_to_image>  # Process one file")
        print("  python3 unr3d4ct.py --watch          # Process everything in 'drop_zone'")
        print("  python3 unr3d4ct.py --clean          # Delete all exported results")
    elif sys.argv[1] == "--clean":
        clean_exports()
    elif sys.argv[1] == "--watch":
        run_dropzone()
    else:
        process_image(sys.argv[1])
        subprocess.run(["open", "unr3d4ct_exports"])
