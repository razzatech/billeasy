'use strict';

angular.module('Enrollment')

.factory('EnrollmentService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.renew_token = function (callback) {

			$http.get('http://billeasy.razzatech.com/api/handler.py/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };
		
		service.fetch_merchants = function (callback) {
			$http.get('http://billeasy.razzatech.com/api/handler.py/fetch_merchants?token='+localStorage.getItem("token"))
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

        service.enroll = function (merchant_code, account_number, custom_name, callback) {
			$http.post('http://billeasy.razzatech.com/api/handler.py/enroll', { merchant_code: merchant_code, merchant_account_number: account_number, custom_name : custom_name, token: localStorage.getItem("token")}, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
			.success(function (response) {
               callback(response);
			});
        };
		

        return service;
    }])

