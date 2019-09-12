<?PHP
require_once("./include/membersite_config.php");

if(isset($_POST['submitted']))
{
   if($fgmembersite->RegisterUser())
   {
        $fgmembersite->RedirectToURL("thank-you.html");
   }
}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>
    <title>Contact us</title>
    <link rel="STYLESHEET" type="text/css" href="style/fg_membersite.css" />
    <script type='text/javascript' src='scripts/gen_validatorv31.js'></script>
    <link rel="STYLESHEET" type="text/css" href="style/pwdwidget.css" />
    <script src="scripts/pwdwidget.js" type="text/javascript"></script>     
    <link href='http://serve.fontsproject.com/css?family=Alef:400'
      rel='stylesheet' type='text/css'>
            <meta 
     name='viewport' 
     content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' 
/>
      <style type="text/css">
    body {background:none transparent;
    }
    </style>

</head>
<body>

<!-- Form Code Start -->
<center>
<div id='fg_membersite'>
        
<center>
<form id='register' action='<?php echo $fgmembersite->GetSelfScript(); ?>' method='post' accept-charset='UTF-8'>
<fieldset >

<h2>?רוצים להצטרף להסעה</h2>
<h4>כיכר רבין</h4>
<h4>שעת יציאה: 18:30</h4>
<input type='hidden' name='submitted' id='submitted' value='1'/>

<input type='text'  class='spmhidip' name='<?php echo $fgmembersite->GetSpamTrapInputName(); ?>' />

<div><span class='error'><?php echo $fgmembersite->GetErrorMessage(); ?></span></div>
<div class='container'>
    <label for='name' >:שם מלא </label><br/>
    <input type='text' name='name' id='name' value='<?php echo $fgmembersite->SafeDisplay('name') ?>' maxlength="50" align="right"/><br/>
    <span id='register_name_errorloc' class='error'></span>
</div>
<div class='container'>
    <label for='phonenum' >:טלפון</label><br/>
    <input type='text' name='phonenum' id='phonenum' value='<?php echo $fgmembersite->SafeDisplay('phonenum') ?>' maxlength="10" type="number"/><br/>
    <span id='register_phonenum_errorloc' class='error'></span>
</div>
<div class='container'>
    <label for='num' >:מספר אנשים</label><br/>
    <input type='text' name='num' id='num' value='<?php echo $fgmembersite->SafeDisplay('num') ?>' maxlength="2" type="number"/><br/>
    <span id='register_num_errorloc' class='error'></span>
</div>
<div class='container'>
    <input type='submit' name='Submit' value='שלח/י' />
</div>

</fieldset>
</form>
<br>
</center>

<!-- client-side Form Validations:
Uses the excellent form validation script from JavaScript-coder.com-->

<script type='text/javascript'>
// <![CDATA[
    var pwdwidget = new PasswordWidget('thepwddiv','password');
    pwdwidget.MakePWDWidget();
    
    var frmvalidator  = new Validator("register");
    frmvalidator.EnableOnPageErrorDisplay();
    frmvalidator.EnableMsgsTogether();
    frmvalidator.addValidation("name","req","Please provide your name");

    frmvalidator.addValidation("email","req","Please provide your email address");

    frmvalidator.addValidation("email","email","Please provide a valid email address");

// ]]>
</script>

<!--
Form Code End (see html-form-guide.com for more info.)
-->

</body>
</html>