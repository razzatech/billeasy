'use strict';

angular.module('Bills')

.factory('BillsService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.renew_token = function (callback) {
			$http.get('http://billeasy.razzatech.com/api/handler.py/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };
		
		service.fetch_accounts = function (callback) {
			$http.get('http://billeasy.razzatech.com/api/handler.py/fetch_billing_accounts?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };
		
		service.add_bill = function (account_id, bill_number, transaction_type, bill_date, due_date, beginning_balance, amount_due, amount_paid, ending_balance, callback) {

            var POST_data = {
				account_id:account_id,
				bill_number:bill_number,
                transaction_type:transaction_type,
                bill_date:bill_date,
                due_date:due_date,
                beginning_balance:beginning_balance,
                amount_due:amount_due,
                amount_paid:amount_paid,
                ending_balance:ending_balance,
				token: localStorage.getItem("token")
            }

            $http.post('http://billeasy.razzatech.com/api/handler.py/add_bill', POST_data, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
            .success(function (response) {
				callback(response);
            });
        };
		
		
        service.fetch_bills = function (callback) {
			$http.get('http://billeasy.razzatech.com/api/handler.py/fetch_bills?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };
		
        return service;
    }])

