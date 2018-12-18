
# Pkg.add("DataFrames")

using DataFrames

key = "2013/06/21"
# openfile="/Volumes/Untitled\ 1/bousai_twitter/bousai_201310-201306.csv"
openfile="/Volumes/usb/bousai_twitter/bousai_201310-201306.csv"
savefile="/Volumes/usb/bousai_twitter/bousai_"*replace(key,"/","")*".csv"

# 指定した日付を抽出
open(savefile, "w") do sf
    open(openfile,"r") do of
        for (index,line) in enumerate(eachline(of))
            if index == 1
                println(line)
            end
            
            line_ts = split(line,',')[3]
            if contains(line_ts, key)
                tmp = replace(line_ts,'/','-')
#                 println(tmp)
                println(sf,replace(line,line_ts,tmp))
            end
        end
    end
end


