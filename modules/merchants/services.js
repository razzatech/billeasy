'use strict';

angular.module('Merchants')

.factory('MerchantsService',
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
		
        service.fetch_bills = function (callback) {
/*
			$http.get('http://joshuabalagapo.pythonanywhere.com/api/fetch_bills?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
*/
        };

		service.add_merchant = function (merchant_code, short_name, full_name, contact_person, contact_number, address, email, callback) {

            var POST_data = {
                merchant_code:merchant_code,
                short_name:short_name,
                full_name:full_name,
                contact_person:contact_person,
                contact_number:contact_number,
                address:address,
                email:email
            }

            $http.post('http://billeasy.razzatech.com/api/handler.py/add_merchant', POST_data, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
            .success(function (response) {
				callback(response);
            });
        };
		
        return service;
    }])

