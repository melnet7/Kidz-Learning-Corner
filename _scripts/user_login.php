<?php
if (isset($_POST['submit'])) {
    if (isset($_POST['name']) && isset($_POST['password']) &&
        isset($_POST['age']) && isset($_POST['email']) &&
        //isset($_POST['phoneCode']) && isset($_POST['phone'])) {
        
        $name = $_POST['name'];
        $password = $_POST['password'];
        $age = $_POST['age'];
        $email = $_POST['email'];
        //$phoneCode = $_POST['phoneCode'];
        //$phone = $_POST['phone'];
        $host = "localhost";
        $dbName = "root";
        $dbPassword = "";
        $dbName = "useraccounts";
        //$conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);
		$conn = new mysqli($host, $dbName, $dbPassword);
        if ($conn->connect_error) {
            die('Could not connect to the database.');
        }
        else {
            $Select = "SELECT email FROM register WHERE email = ? LIMIT 1";
            //$Insert = "INSERT INTO register(username, password, gender, email, phoneCode, phone) values(?, ?, ?, ?, ?, ?)";
            $Insert = "INSERT INTO register(name, password, age, email) values(?, ?, ?, ?, ?, ?)";
			$stmt = $conn->prepare($Select);
            $stmt->bind_param("s", $email);
            $stmt->execute();
            $stmt->bind_result($resultEmail);
            $stmt->store_result();
            $stmt->fetch();
            $rnum = $stmt->num_rows;
            if ($rnum == 0) {
                $stmt->close();
                $stmt = $conn->prepare($Insert);
                $stmt->bind_param("ssssii",$name, $password, $age, $email);
                if ($stmt->execute()) {
                    echo "New record inserted sucessfully.";
                }
                else {
                    echo $stmt->error;
                }
            }
            else {
                echo "Someone already registered using this email.";
            }
            $stmt->close();
            $conn->close();
        }
    }
    else {
        echo "All field are required.";
        die();
    }
}
else {
    echo "Submit button is not set";
}
?>


