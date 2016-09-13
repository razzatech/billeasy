'use strict';

angular.module('Bills')

.controller('BillsController',
    ['$scope', '$location', 'BillsService',
    function ($scope, $location, BillsService) {	
		$scope.transaction_types=[{"label": "BILLING"},{"label": "PAYMENT"},{"label": "ADJUSTMENT"}];
		$scope.transaction_type=$scope.transaction_types[0];
		
		$scope.accounts=[];
		
		$scope.bills=[];
		
		$scope.show_uploader=false;
	
	    //renew token every 5 seconds
		(function renew_token() {
			BillsService.renew_token(function(response) {
				if(response.success) {
					if($location.path().startsWith('/bills'))
					{
						localStorage.setItem("token", response.token);
						console.log("Token renewed.");

						setTimeout(function()
						{
							renew_token();
						}, 5000);
					}
				} else {
					localStorage.clear();
					$location.path('/login');
					console.log("Authentication failed. Redirecting to login page.")
				}
			});
		})();
		
		//fetch billing accounts for select box
		(function fetch_accounts() {
			BillsService.fetch_accounts(function(response) {
				if(response.success)
				{
					$scope.accounts=response.accounts;
					$scope.selected_account=$scope.accounts[0];
					console.log("Accounts retrieved.");
				}
			});
		})();
		
		//fetch bills
        $scope.fetch_bills = function () {
            BillsService.fetch_bills(function(response) {
				if(response.success)
				{
					$scope.bills=response.bills;
					console.log("Bills updated.");
				}
			});
        }
        $scope.fetch_bills();
		
		//add new row
		$scope.add_bill = function () {
            $scope.dataLoading = true;
			var a=$scope.account.account_id;
			var b=$scope.bill_number;
			var c=$scope.transaction_type.label;
			var d=$scope.bill_date;
			var e=$scope.due_date;
			var f=$scope.beginning_balance;
			var g=$scope.amount_due;
			var h=$scope.amount_paid;
			var i=$scope.ending_balance;
			
            BillsService.add_bill(a, b, c, d, e, f, g, h, i, function(response) {
                if(response.success) {
                    $scope.dataLoading = false;
					alert("Bill added");
					
					$scope.bill_number="";
					$scope.transaction_type.label="";
					$scope.bill_date="";
					$scope.due_date="";
					$scope.beginning_balance="";
					$scope.amount_due="";
					$scope.amount_paid="";
					$scope.ending_balance="";					
					
					$scope.fetch_bills();
                } else {
					alert("Input error!")
				}
            });
        };
		
		//upload csv
		$scope.upload_csv = function() {
			$scope.show_uploader=true;
		}
		
		
		//"Logout" link
		$scope.logout = function() {
			localStorage.clear();
			console.log("User logged out.");
			$location.path('/');			
		}
    }]);