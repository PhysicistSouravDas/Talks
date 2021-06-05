set terminal pngcairo size 350,262 enhanced font 'Verdana,10'
# set terminal pngcairo size 1920,1080 enhanced font 'Verdana,10'

# color definitions
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 2 # --- blue

unset key
# set border 0
unset tics
set view 342,0
set xrange [-150:150]
set yrange [-150:150]
system('mkdir random_walk')
# plot (x, y)
n=0
do for [ii=1:10000] {
    n=n+1
    set output sprintf('random_walk/img%05.0f.png',n)
    plot 'Random_Walk.dat' every ::1::ii w l ls 1, \
         'Random_Walk.dat' every ::ii::ii w p ls 1
}