def message_text(content, title):
    html = '''<!DOCTYPE html>
<html lang="en" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background: #FFFFFF;margin: 0 auto !important;padding: 0 !important;height: 100% !important;width: 100% !important;">
<head style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
    <meta charset="utf-8" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"> 
    <meta name="viewport" content="width=device-width" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"> 
    <meta name="x-apple-disable-message-reformatting" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">  
    <title style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;"></title> 
    <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'> 

</head>

<body width="100%" style="margin: 0 auto !important;padding: 0 !important;mso-line-height-rule: exactly;background-color: #FFFFFF;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background: #FFFFFF;font-family: 'Poppins', sans-serif;font-weight: 400;font-size: 15px;line-height: 1.8;color: rgba(0,0,0,.4);height: 100% !important;width: 100% !important;">
	<center style="width: 100%;background-color: #FFFFFF;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
    <div style="display: none;font-size: 1px;max-height: 0px;max-width: 0px;opacity: 0;overflow: hidden;mso-hide: all;font-family: sans-serif;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
      &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
    </div>
    <div style="max-width: 600px;margin: 0 auto;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;" class="email-container">
      <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;border-spacing: 0 !important;border-collapse: collapse !important;table-layout: fixed !important;">
      	<tr style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
          <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background: #ffffff;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;">
          	<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;border-spacing: 0 !important;border-collapse: collapse !important;table-layout: fixed !important;margin: 0 auto !important;">
          		<tr style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
          			<td class="logo" style="text-align: center;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;">
			            <h1 style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;font-family: 'Poppins', sans-serif;color: #000000;margin-top: 0;font-weight: 400;margin: 0;"><a href="#" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;text-decoration: none;color: #17bebb;font-size: 24px;font-weight: 700;font-family: 'Poppins', sans-serif;"><img src="https://logos.mviyotechnologies.com/mviyo/final-09.png" width="400" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;-ms-interpolation-mode: bicubic;"></a></h1>
			          </td>
          		</tr>
          	</table>
          </td>
	      </tr><!-- end tr -->
				<tr style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
          <td valign="middle" class="hero bg_white" style="padding: 2em 0 4em 0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background: #ffffff;position: relative;z-index: 0;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;border-spacing: 0 !important;border-collapse: collapse !important;table-layout: fixed !important;margin: 0 auto !important;">
            	<tr style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
            		<td style="padding: 0 2.5em;text-align: center;padding-bottom: 3em;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;">
            			<div class="text" style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;color: rgba(0,0,0,.3);">
            				<h2 style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;font-family: 'Poppins', sans-serif;color: #000;margin-top: 0;font-weight: 200;font-size: 34px;margin-bottom: 0;line-height: 1.1;">
                    '''+title+'''
                    </h2>
                    <br>
                    <p
                    style="
                        font-size: 15px;
                        font-weight: 400;
                        font-family: 'Roboto', Arial, sans-serif;
                        line-height: 160%;
                    "
                    >
                    '''+content+'''
                    <br>
                    <br>
                    
                    </p>
            			</div>
            		</td>
            	</tr>
            	
            </table>
          </td>
	      </tr><!-- end tr -->
      <!-- 1 Column Text + Button : END -->
      </table>
      <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;border-spacing: 0 !important;border-collapse: collapse !important;table-layout: fixed !important;">
        <tr style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
          <td class="bg_light" style="text-align: center;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;background: rgba(251, 250, 250, 0.8);mso-table-lspace: 0pt !important;mso-table-rspace: 0pt !important;">
          	<p style="-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">No longer want to receive these email? You can <a href="#" style="color: rgba(0,0,0,.8);-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;text-decoration: none;">Unsubscribe here</a></p>
          </td>
        </tr>
      </table>

    </div>
  </center>
</body>
</html>'''
    return html




def message():
    return f"""
Thank you for accepting the invitation to Mviyo Technologies Launch Event. Your presence is greatly appreciated.
<br />
<br />
Canapés and cocktails will be provided for you.
<br />
<br />
<b>
Kind regards,
</ b>
<br />
<br />
<b>
The Mviyo Team
</ b>
<br />
<br />
 """

