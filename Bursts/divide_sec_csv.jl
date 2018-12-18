# Pkg.add("DataFrames")
using DataFrames

date = "0621"
# openfile="/media/usb/bousai_twitter/bousai_20130915.csv"
openfile="/Volumes/usb/bousai_twitter/bousai_2013" + date + ".csv"
savefile="./time.csv"

# 指定した日付を抽出
open(savefile, "w") do sf
    open(openfile,"r") do of
        for (index,line) in enumerate(eachline(of))
            if index == 1
                println(sf,"time")
            else
                line_ts = split(line,',')[3]
                line_ts = replace(line_ts, "/", "-")
                println(sf,line_ts)
            end
        end
    end
end

df = DataFrames.readtable(savefile)
sort!(df)

savefile="./ms_time.csv"

open(savefile,"w") do sf
    # println(df)
    time_array = df[1]
#     time_array = flipdim(df[1][1:end],1)
#     println(time_array)

    old_line = "\n"
    line_count = 1

    println(sf,"time")
    for (i,line) in enumerate(time_array)
        # 秒単位で一致したら、下の桁に等間隔で分散させる

        # 拾ってきた行を形成

        # println(line)

        # 行数カウント
        if line == old_line
            line_count += 1
        else
            # println(old_line*","*string(line_count))

            # 等間隔に小数点以下に広げる
            tmp = collect(0:1/line_count:1)[1:end-1]

            # 1ms単位に変換する
            tmp = map(round,tmp*10^6)/10^6

            # ms単位で格納
            for ms in tmp
                if i > 1
                    println(sf,old_line*string(ms)[2:end])
                end
            end

            line_count = 1
            old_line = line
        end
    end
    
    tmp = collect(0:1/line_count:1)[1:end-1]
    for ms in tmp
        println(sf,old_line*string(ms)[2:end])
    end
end

df = DataFrames.readtable(savefile)
