import os
import re


class Renamer:

    def __init__(self, _path) -> None:
        self.path = _path

    def other(self):
        for e in range(47, 71):
            n = 46
            s = str(e - n)
            if (e - n < 10):
                s = "0" + s
            path1 = "Z:\漫\魔卡少女樱\S03\\"
            name1 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + str(e) + "][1080P][BDRip][HEVC-10bit][FLAC].mkv"
            name2 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + s + "][1080P][BDRip][HEVC-10bit][FLAC].mkv"
            os.rename(path1 + name1, path1 + name2)
            name1 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + str(e) + "][1080P][BDRip][HEVC-10bit][FLAC].sc.ssa"
            name2 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + s + "][1080P][BDRip][HEVC-10bit][FLAC].sc.ssa"
            os.rename(path1 + name1, path1 + name2)
            name1 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + str(e) + "][1080P][BDRip][HEVC-10bit][FLAC].tc.ssa"
            name2 = "[DBD-Raws][4K Remaster][魔卡少女樱][S03E" + s + "][1080P][BDRip][HEVC-10bit][FLAC].tc.ssa"
            os.rename(path1 + name1, path1 + name2)

    def netflix(self):
        path1 = "Z:\剧\弥留之国的爱丽丝\Alice.in.Borderland.S02.JAPANESE.1080p.WEBRip.x265-RARBG\Subs\\"
        for e in range(1, 9):
            n = 0
            s = str(e - n)
            if (e - n < 10):
                s = "0" + s
            path2 = "Alice.in.Borderland.S02E" + s + ".JAPANESE.1080p.WEBRip.x265-RARBG\\"
            name1 = "37_Chinese.srt"
            name2 = "Alice.in.Borderland.S02E" + s + ".JAPANESE.1080p.WEBRip.x265-RARBG.chs.srt"
            os.rename(path1 + path2 + name1, path1 + path2 + name2)

    def sc_tc2chs_cht(self):
        s_new = ""
        for root, dirs, file_names in os.walk(self.path):
            for s in file_names:
                s_new = s.replace(".sc", ".chs")
                if s_new != s:
                    os.rename(self.path + s, self.path + s_new)
                    continue

                s_new = s.replace(".tc", ".cht")
                if s_new != s:
                    os.rename(self.path + s, self.path + s_new)
                    continue

                s_new = s.replace(".SC", ".chs")
                if s_new != s:
                    os.rename(self.path + s, self.path + s_new)
                    continue

                s_new = s.replace(".TC", ".cht")
                if s_new != s:
                    os.rename(self.path + s, self.path + s_new)
                    continue

    def episode(self, season):
        for root, dirs, file_names in os.walk(self.path):
            for s in file_names:
                match = re.search(r"\[\d+\]", s)
                if match:
                    e = match.group()
                    s_new = re.split(r"\d+\]", s)
                    e = re.search(r"\d+\]", s).group()
                    if season<10:
                        e = "S0" + str(season) + "E" + e
                    else:
                        e = "S" + str(season) + "E" + e
                    os.rename(self.path + s, self.path + s_new[0] + e + s_new[1])

                match = re.search(r"- \d+", s)
                if match:
                    i = match.span()[0] + 1
                    e = re.search(r"\d+\]", s).group()
                    if season<10:
                        e = "S0" + str(season) + "E"
                    else:
                        e = "S" + str(season) + "E"
                    s1 = s[0:i]
                    s2 = s[i + 1:]
                    os.rename(self.path + s, self.path + s1 + e + s2)
