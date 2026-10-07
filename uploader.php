<?php
// PHP upload handler server mock
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo json_encode(["status" => "success", "message" => "IPA parsed successfully"]);
}
?>