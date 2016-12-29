curDir=./
echo begin git add $curDir
git add $curDir
echo begin git pull $curDir
git pull $curDir
##date 命令赋值使用$()
comment=$(date "+%Y-%m-%d")
echo begin commit -m $comment
git commit -m $comment
echo begin git push $curDir
git push
