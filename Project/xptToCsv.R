options(stringsAsFactors=F, scipen = 999)

pkg = 'Hmisc'
if (!require(pkg, character.only = TRUE)) {
  install.packages(pkg)
  library(pkg, character.only = TRUE)
}


brfss <- sasxport.get("./LLCP2014.XPT ")
write.csv(brfss, file = "./brfss2014.csv")

brfss <- sasxport.get("./LLCP2021.XPT ")
write.csv(brfss, file = "./brfss2021.csv")

brfss <- sasxport.get("./LLCP2020.XPT ")
write.csv(brfss, file = "./brfss2020.csv")

brfss <- sasxport.get("./LLCP2019.XPT ")
write.csv(brfss, file = "./brfss2019.csv")
