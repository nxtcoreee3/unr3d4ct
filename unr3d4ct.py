import cv2
import numpy as np
import os
import sys
import subprocess

def unr3d4ct(image_path):
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"[-] Error: Could not find or open '{image_path}'")
        return

    
    output_dir = "unr3d4ct_exports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"[*] Initializing unr3d4ct scan on: {image_path}")

    
    alphas = [1.5, 2.5, 4.0]  
    betas = [-70, -30, 0, 30, 70]
    gammas = [0.2, 0.5, 1.0, 1.8]

    total_variants = len(alphas) * len(betas) * len(gammas)
    processed = 0

    for a in alphas:
        for b in betas:
            
            adjusted = cv2.convertScaleAbs(img, alpha=a, beta=b)
            
            for g in gammas:
                
                inv_gamma = 1.0 / g
                table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
                final = cv2.LUT(adjusted, table)
                
              
                out_file = f"{output_dir}/v_a{a}_b{b}_g{g}.jpg"
                cv2.imwrite(out_file, final)
                
                processed += 1
                sys.stdout.write(f"\r[+] Processing: {processed}/{total_variants} variants generated")
                sys.stdout.flush()

    print(f"\n[!] Scan complete. Results saved in '{output_dir}/'")

    
    try:
        subprocess.run(["open", output_dir])
        subprocess.run(["afplay", "/System/Library/Sounds/Tink.aiff"])
    except Exception:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unr3d4ct.py <image_path>")
    else:
        unr3d4ct(sys.argv[1])
