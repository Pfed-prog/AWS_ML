# AWS_ML

Deployed Using Elastic Beanstalk at http://app-env.eba-hxn3i6de.us-east-2.elasticbeanstalk.com/

We are accessing Uniswap V3 GraphQL at https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3?selected=playground to obtain historical data for the chosen token. he Default token is Uniswap.

Next we use model the time-series data to predict token price for the N number of timestamps. Default is 15 periods.

We have Used Arima(1,1,0) model since it has maths foundation and differences the data to make stationary.

## References

[DSPYT: Time series data – An easy introduction](https://dspyt.com/time-series-data-an-easy-introduction/)

[Caleb Curry: Python + Flask Deploy to Amazon Web Services Elastic Beanstalk (CI/CD with Git)](https://www.youtube.com/watch?v=4tDjVFbi31o)
