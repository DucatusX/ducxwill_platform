register_subject = """Please Confirm Your E-mail Address"""

register_text = """{subsite_name} team welcomes you!

You're receiving this e-mail because user {user_display} has entered this e-mail address to connect to their account.

To confirm the registration, click on the link below:

{activate_url}

Best regards!
{subsite_name} Team."""


password_reset_subject = """Password reset on {subsite_name} """
password_reset_text = """
You're receiving this email because you requested a password reset for your user account at {subsite_name}.

Please go to the following page and choose a new password:

{password_reset_url}

Your username, in case you've forgotten: {user_display}

Thanks for using our site!

{subsite_name} Team."""

common_subject = """Your contract is ready"""
common_text = """Hello,

We are happy to inform you that your contract was successfully created and deployed to {network_name} network.
{contract_type_name}: {link}

Please contact support@mywish.io if you need if you have any questions.

Best wishes,
MyWish Team."""

ico_subject = """Your contract is ready"""
ico_text = """Hello,

We are happy to inform you that your contract was successfully created and deployed to {network_name} network.
Token contract: {link1}
Crowdsale contract: {link2}

Please contact support@mywish.io if you have any questions.

Best wishes,
MyWish Team."""

create_subject = """Your contract is ready for deployment"""
create_message = """Congratulations!

Your contract is created and ready for deployment to {network_name}.

If you have any questions or want to get free promotion of your project in MyWish social channels please contact support@mywish.io.

Thank you for using MyWish.
"""


heir_subject = """MyWish notification"""
heir_message = """Hello!

In accordance with the contract created on MyWish platform, Funds have been transfered to address "{user_address}" :  "{link_tx}"

If you have any questions, please contact support@mywish.io"""

postponed_subject = """ATTENTION! POSTPONED CONTRACT"""
postponed_message = """Contract {contract_id} change state on 'POSTPONED' """

remind_subject = """Reminder to confirm ???Live??? status"""
remind_message = """Hello,

We would like to remind you to confirm your ???live??? status for the contract.
Contract will be executed if no confirmation during the next {days} days.

You can see the contract here: https://contracts.mywish.io

If you have any questions please contact support@mywish.io

Best wishes,
MyWish Team
"""
carry_out_subject = """The Will contract is completed"""
carry_out_message = """Hello,

In accordance with Will contract funds have been transferred successfully.

If you have any questions please contact support@mywish.io

Best wishes,
MyWish Team
"""


authio_subject = """MyWish - Request for brand report"""
authio_message = """Hello!

We want to inform you that the user {email} has created a request to check
the smart contract created on the MyWish platform and get a branded report.

Contract parameters (Source code):

1) Token address: {address}
2)Token name: {token_name}
3) Token symbol: {token_short_name}
4) Decimals: {decimals}
5) Type of Token: {token_type}
6) Token Owner: {admin_address}
7) Mint/Freeze tokens: {mint_info}
Please contact support@mywish.io if you have any questions.

Best wishes,
MyWish Team.
"""

authio_google_subject = """Branded Audit Report: Project details request"""
authio_google_message = """Hello!

Thank you for using our service.

Your contract is ready for the report preparation.

If you have any questions - please mail to support@mywish.io. We will contact you as soon as possible.

Thank you,
MyWish Team
"""

ducatus_admin_confirm_subject = """MyWish - Request for deploying contract to DucatusX Mainnet"""
ducatus_admin_confirm_ico_text = """Hello!

We want to inform you that the user {email} has created a contract and wanted
to deploy it to DucatusX Main Network.

Contract type: DucatusX Crowdsale (ICO)
Contract parameters (Source code):

Token details:
1) Token name: {token_name}
2) Token symbol: {token_short_name}
3) Decimals: {decimals}
4) Type of Token: {token_type}
5) Token Owner: {admin_address}

Crowdsale details:
1) Token rate: {token_rate}
2) Hard cap tokens: {hard_cap_tokens}
3) Soft cap tokens: {soft_cap_tokens}
4) Start date: {start_date}
5) Stop date: {stop_date}
6) Transferable: {transferable}
7) Investments storage address: {cold_wallet_address}
8) Whitelist: {whitelist}
9) Changing dates: {changing_dates}


To see more details, confirm or cancel contract - click here: {confirm_url}

Please contact support@mywish.io if you have any questions.

Best wishes,
MyWish Team.
"""
ducatus_admin_confirm_token_text = """Hello!

We want to inform you that the user {email} has created a contract and wanted
to deploy it to DucatusX Main Network.

Contract type: DucatusX Token
Contract parameters (Source code):

1) Token name: {token_name}
2) Token symbol: {token_short_name}
3) Decimals: {decimals}
4) Type of Token: {token_type}
5) Token Owner: {admin_address}


To see more details, confirm or cancel contract - click here: {confirm_url}

Please contact support@mywish.io if you have any questions.

Best wishes,
MyWish Team.
"""
