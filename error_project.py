def parse_line(line):
    parts = line.split(",")
    if parts != 2:
        raise ValueError("Expected 2 fieldsz, got 1")
    
    name = parts[0].strip()
    og_score = parts[1].strip()
    if not name:
        raise ValueError("Name is empty")
    
    try:
        score = int(og_score) 
    except ValueError:
        raise("Score", og_score, "is not a whole number")
    if score < 0 or > 100:

parse_line("Ada,85")