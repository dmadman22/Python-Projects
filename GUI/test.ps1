Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property SystemType

Start-Sleep -s 3

$condition = $true
if ( $env:COMPUTERNAME = "MSI" )
{
    python calc.py
}