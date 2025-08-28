import math

def aspect_ratio(width: int, height: int) -> str:
    gcd = math.gcd(width, height)  # наибольший общий делитель
    return f"{width // gcd}:{height // gcd}"

if __name__ == "__main__":
    # пример с Pixel 9 Pro XL
    w, h = 1280, 2856
    atalon = aspect_ratio(w, h)
    print(f"{w}x{h} -> {aspect_ratio(w, h)}")
    # можно протестировать и другие варианты
    sss = ''
    sss3 = 900
    sss1 = 1000
    while sss != atalon:
        sss = aspect_ratio(sss3, sss1)
        # if sss.startswith("160"):
        #     print(f"1080x{sss1} -> {sss}")
        sss1 += 1
        if sss1 == 3000:
            sss3 += 1
            sss1 = 1000
        # if sss1 == 2000: break
        if str(sss) == str(atalon): 
            print(sss3, sss1)
            print(f"{sss3}x{sss1} -> {sss}")
            break