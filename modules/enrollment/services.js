'use strict';

angular.module('Enrollment')

.factory('EnrollmentService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.renew_token = function (callback) {

			$http.get('http://joshuabalagapo.pythonanywhere.com/api/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

        service.fetch_accounts = function (callback) {

			$http.get('http://joshuabalagapo.pythonanywhere.com/api/fetch_accounts?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

        service.enroll = function (biller_name, account_number, callback) {
			$http.post('http://joshuabalagapo.pythonanywhere.com/api/enroll', { biller_name: biller_name, account_number: account_number, token: localStorage.getItem("token")}, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
			.success(function (response) {
			    console.log(biller_name +","+ account_number +","+ localStorage.getItem("token"));

                callback(response);
			});
        };

        return service;
    }])

