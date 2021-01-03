#First, we insert the database from Air France
library(readxl)
AF_DB <- read_excel("C:/Users/Usuario/Desktop/Hult/MsBAN/R/air france business case/Air France Case Spreadsheet Supplement.xls", 
                    sheet = "DoubleClick")
View(AF_DB)
#we need to change the missing values of bid strat to "no strat"
AF_DB$`Bid Strategy`[is.na(AF_DB$`Bid Strategy`)] = "No Strategy"
#we check for missing values
sum(is.na(AF_DB)) #we have 0 missing values now
#Since we will be adding parameters, we need to make sure that there are no 0 values
AF_DB <- AF_DB[which(AF_DB$`Total Cost` !=0), ] #we basically eliminate only 1 row with this
#Now we need to add some important parameters

#Creating new Variable: Net Revenue
AF_DB$Net_Revenue <- (AF_DB$Amount - AF_DB$`Total Cost`)

#Creating new Variable: ROA
AF_DB$ROA <- (AF_DB$Net_Revenue / AF_DB$`Total Cost`)

#creating new variable: Cost per Booking, we need to consider that if total volume of
#bookings is 0, then we would get and inf. Therefore, if tot vol of bookings is 0,
#we will be have "NA" on the cost per booking column

for(i in 1:nrow(AF_DB)){
if (AF_DB$`Total Volume of Bookings`[i] == 0){
  AF_DB$CostPerBooking[i] <- "NA"
}else {AF_DB$CostPerBooking[i] <- (AF_DB$`Total Cost`[i] / 
                                       AF_DB$`Total Volume of Bookings`[i])}#ending if loop
}#ending the for loop

#creating new variable: Average Revenue per Booking
#we apply the same logic as with CostPerBooking
for(i in 1:nrow(AF_DB)){
if(AF_DB$`Total Volume of Bookings`[i] == 0){
  AF_DB$AverageRevPerBooking[i] <- "NA"
}else {AF_DB$AverageRevPerBooking <- (AF_DB$Amount[i] / 
                                        AF_DB$`Total Volume of Bookings`[i])}#ending if loop
}#ending the for loop

#creating new variable: Probability of booking
AF_DB$BookingProb <- ((AF_DB$`Engine Click Thru %` * AF_DB$`Trans. Conv. %`) /
                             (100 * 100))

#we transform the variable Camp_code to factor and then to numeric
#in order to better apreciate the number of campaigns
AF_DB$Camp_code <- as.numeric(as.factor(AF_DB$Campaign))

#we will create a function that give us the min, max and mean of a column and 
#the %of "NA"values

sub1 <- AF_DB[which(AF_DB$Camp_code == 1), ]
sub1$CostPerBooking <-   as.numeric(sub1$CostPerBooking)
nrow(sub1)
is.na(sub1$CostPerBooking)
sum(is.na(sub1$CostPerBooking))
Na <- sum(is.na(sub1$CostPerBooking)) / nrow(sub1)
print(Na)

tot_rev <- sum(sub1$Net_Revenue)
winrate <- nrow(sub1[which(sub1$Net_Revenue > 0),])/nrow(sub1)
print(tot_rev)
print(winrate)


#we create an empty data frame
comp_table <- data.frame() 
#change the 24 for the number of campaigns
for(j in 1:24){
  for (i in 1:nrow(AF_DB)){

  
  if(AF_DB$Camp_code[i] == j){
    
    pub <- AF_DB$`Publisher Name`[i]
    New_value <- AF_DB$Campaign[i]
    tot_revs <- sum(AF_DB[which(AF_DB$Camp_code == j),]$Net_Revenue)
    winrates <- nrow(AF_DB[which(AF_DB$Camp_code == j & AF_DB$Net_Revenue > 0) ,])/
                       nrow(AF_DB[which(AF_DB$Camp_code == j),])
    Tot_ROA <- sum(AF_DB[which(AF_DB$Camp_code == j),]$ROA)
    CPC <- mean(AF_DB[which(AF_DB$Camp_code == j),]$`Avg. Cost per Click`)
    }#closing if
    #create table
  
  }
  comp_table[j,1] <- pub
  comp_table[j,2] <- New_value
  comp_table[j,3] <- tot_revs
  comp_table[j,4] <- winrates
  comp_table[j,5] <- Tot_ROA
  comp_table[j,6] <- CPC #average cost per click
  
}#closing for
#renaming the columns names
names(comp_table) <- c( "Publisher Name", "Campaign Name", "Total Revenue", "Acceptance %",
                        "ROA", "Avg. Cost per Click")

AF_DB$`Keyword Group`<- as.factor(AF_DB$`Keyword Group`)
