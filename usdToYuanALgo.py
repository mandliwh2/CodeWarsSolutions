def usdcny(usd):
    usd = float(usd)
    chineseYuan = usd *  6.75
    final = str(format(chineseYuan, ".2f")) + " Chinese Yuan"
    return final
