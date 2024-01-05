# Cloud-Resource-Consumption-Analytics

This is a analytics use case for cloud consumption analytics for a whole tenant and can  be used for any Microsoft-Partner

The Architecture:

Azure Functions:

     gets Keys and Secrets stored in the Azure KeyVault, authenticates with the Microsofts-Partnercenter API, gets  the Datasets and uploads it to the Storage Account.
     Also its registers the reoccurring reports and the the queries for the API.
     Refer here for more Information for the API:
     https://learn.microsoft.com/en-us/partner-center/insights-programmatic-access-paradigm

Azure Key Vault:

    Holds API-Keys, Report-Ids and Query-Ids

Azure Data Lake:

    funtions as the data lake and the historization for the datasets

Azure Data Factory:

    Takes the dataset and copys it to the staging area in the SQL DataBase
    Updates the Dimensions in the Warehouse via merge Statement, these are held in stored procedures in the SQL-Database
    Updates the fact table in the Warehouse via merge statements, stored in stored procedure

SQL-Database:

    Holds the Data Warehouse.

    Dimensions:

        DimService - distinguishes the Azure Service used
        DimPartner - the partner status of the Subscription
        DimCustomer - The Cutomer of the "Consulting" Firm that implemented Cloud Resources
        DimFieldRevenueAccoutnability
        DimSupscription - Consumption will be splitted under different Subscriptions in the Tenannt, unfortunately you cannot get Consumption on Resourcelevel
    
    Facts:

        Facts table holds the actual dollar amounts and connects the warehouse keys from the dimensions

    

    






