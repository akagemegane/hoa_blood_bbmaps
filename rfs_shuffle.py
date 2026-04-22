import os
import random

def generate_blood_ini():
    # 1. Scan for .map files
    maps = [f for f in os.listdir('.') if f.lower().endswith('.map')]
    
    if not maps:
        print("No .MAP files found in the current directory.")
        return

    # 2. Shuffle the map list
    random.shuffle(maps)

    # 3. Build Header and Episode List
    content = [
        ";=====================================================================",
        "; Blood Refreshed Supply Map Rotation",
        ";=====================================================================",
        "[Install]",
        "SourceDir=:.",
        "",
        "[MenuSounds]",
        "Song = cblood7",
        "Track = 5",
        "TrackStartTime = 46.020",
        "",
        "[Episode1]",
        "Title = Server"
    ]
    
    # Add Map1, Map2, etc. to [Episode1]
    for i, map_file in enumerate(maps):
        map_name = os.path.splitext(map_file)[0]
        content.append(f"Map{i+1} = {map_name}")

    content.append("")
    content.append(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    content.append("; Map Rotation Definitions")
    content.append("")

    # 4. Generate map sections named after the file, pointing to next index
    for i, map_file in enumerate(maps):
        current_map_name = os.path.splitext(map_file)[0]
        current_index = i + 1
        
        content.append(f"[{current_map_name}]")
        content.append(f"Title = {current_map_name}")
        
        # Determine the Ending value
        if current_index < len(maps):
            # Point to the next index (e.g., if at 1, point to 2)
            next_idx = current_index + 1
            content.append(f"EndingA = {next_idx}")
            content.append(f"EndingB = {next_idx}")
        else:
            # Last map points back to 1
            content.append(f"EndingA = 1")
            content.append(f"EndingB = 1")
        content.append("")

    # 5. Write to SERVER.INI
    try:
        with open('SERVER.INI', 'w') as f:
            f.write("\n".join(content))
        print(f"Successfully generated SERVER.INI with {len(maps)} maps.")
    except IOError as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    generate_blood_ini()