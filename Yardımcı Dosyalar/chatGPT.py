from pyChatGPT import ChatGPT

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..KACSkt5ug9MVhXOd.fR1fW5cBpVivZcPEG_CMI3Gi9pl7tzkUrETsEZRkkGtf6KePYE85171nYWkB9qHVmUFzo5xkZeJYrsE2-OlbRtB0cJMpQou3fu3UlYm3JuVkNfPkx0_TQJNibSxk2iI6gzfv2p_YCMm0kMSV8w5SeKZtY3sKcrQoMfQeM_HOn2_-BnIIKKOryM4o-u2ineOcm44M3vuUhzNdLzNOda_jpyzKWNc6C03MoxxsN65akbU4xk7RbscjfzjH70Kp1EyWkSMmlXb0k_h4uW6pf-Co_IFflE3a2DmNDgqQ_Y-WsuUwNaVgKG6jPYq4dhJZBDbHESqxFAsas8CxMUBGTFsitsE3cIhIxX0L5dDt5Gg2OuB9q012j4Q4mqs6QOt-RXz9M2PJAWmb6aU88j0xuulCYQ8w3zQfKpA9DxS7KL3B7a43aHLwFj5AOWQhXOq_YCFrJGkEhDk-ry4_RJCTUzqMSAPfknMuioKP8au2IAg_A-_JATg32U7OyuNxZcs-qI3oqO7zYYwrPZvRS8oPFMYb4xxKWZhYq7YWBn33J2BPzz04PnlaYBSyXqzwuEdpzW32BZ_PWSkYRR7D3BoAm0btWx8IP45mG5ax9dIhXZl8VUnqbiY9fUUhunmsw14cAehpFkiyGgqxGkWhvvENZZuX4hMVRqCpFRmavi86RQ6q3ZxbE5uyu-7MnFR29M0Fv7_S3gpsLddHmMvWqzNLguxphFerqmBeSTSLrv-m4Lesb6B7JrhfrXCnEen5lM9yEDssgHAz94yx69c38QKgP87YisuRitZ450UH4mFsfWUtJeaxWP2cUU0IZkFLnvosbJ8kIO46TE6eSVScrS5J2XgK4GR49wYoCcaHaQ0Hec6BJE-PUEFPIHjkQPolSRM4rTyh1jyUoPA94DYIwa-JmRMXxOEOmr-tCpJMeA4pdcIhdQ73GHfza_C6rjSgRdf7hXN5Miqunk7tx9a0BdAhYE_L_YXhUT2f-42PE4JYwUqmBdFfZI0guGM_6z-lKmDLgBdrqiDUgsSlhnMBMBOnWt7b9uDLA8St0oda6rhuIzLzYfdp-MLN33Y_iPPR94W0KafzS4ZKUZ_bAXjj6iJ7FaEmYl-mp6fBBI8pcopV5VVgzSEMzmyMG9RXjIS0GdsFgkpRe1q3HThj82TXtALMatPY7pFSxVypdR9NB7jszxH1LIPPkI84gfGv_fWYEaGPRLUbboqcwBhi8IWQzRya7zUITeN9fL-RE087zSMmJz_5UiRJjQDmytJz6Th-pktd8o7EeDYrK3kmGzInEMA-w99YL0jRkmDgsZJ8xsWpm9oxaXs0rmCy6ZhHbHyn9nBBQfyPe-BdnSn4LoDPBgwRb7tIysmwTxDjozmQyvdr6ksIaBKI6z0xkdK51gFSD6nZdsPF1eBqzDgJt7csdmimW1gIbdK2MWKXfcsjfFG-wCO4a31CYfN-be1TTIsyJO4F6iL9XUzSwNj5fmFxzwS2wSa_-MPcThdyVdyiGk9FcI0bGbmblU4GSvcNakQkueHGa5hDeckMm2qm2R5JiHi1DSV55dLn2MCFSlb_yLM3whDYndXSgnSuzOsmT55FpxTRdnZDYgkWa97VLMVkAI9Il56kuVIN44RWuE5NWzscPNO7Osrosmvih_inQ3npmTDGTbnELJx-3zGiycnsC_P6ODepuyNZxz0gYCtsROskj1TcVMH5EiO9riFp8NKzRQC8hOMV8i260rNVHCS8vDO8xGeISwAZznNCOfkbDKmHvi83jR_LEfBDcngOHlZmboMmGMl0JmVdcILeSs-GP1kB1iF03k2CljFuBQGbFcKEt2oYsgZxoPq3-ihmckQ81qARE5SWLC_EjyzT9kJLTmtXl37kYRjfmFAdtRq8WEyCc5RsVaVLyN3oSXNKgsnB8-riBa91rK5UoqB7kSaTQ1NqRwfGUFYaXq4KilxSs2jQlCw1nMxOBqSLUWsmFZRVCE-6Zz42BPTQ9hRugHATLkmgQ7ekfqkRxCk67vKPjWfg1i1kvmL6E5WL007ubFcjI421HU3rGdIop0wqnLuY7dfQtIgeTBorF37es39ypP9AxbFtZnVfUvAAOEkUKEYr1SD6ZnnHJ4ihcU_I8UiRB9_o-4LfVjQC7GvtXH1f_AGCAe2rDbMKxQJk4hEc3OidfYcZISR24eKhHuz_kCeNYF5WOmrizb-Fr5EmPuEMpDBE1UG9moNSiPCIiKXDkRRDJN4HaZx9S3HCZAdSWFC8dfTDlg_lUILSRLhL0TgBftXOCcrKH9r7_SyxWE-2k-v56c1VIErhaFh-16zuLYYZq8hL-fRs3D4PZfzkuBnOz7TfvXmkTBhhZfV6ScybI-W9K9dGSn0aN9pGvBlWxQ.JtYetiWP6iqHPBz3anbkyA'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api1 = ChatGPT(session_token)  # auth with session token
#api2 = ChatGPT(session_token, proxy='http://proxy.example.com:8080')  # specify proxy

resp = api1.send_message('"何を見てるんだ" ne demek')
print(resp['message'])

#api1.reset_conversation()  # reset the conversation
api1.close()  # close the session