#!/usr/bin/env python
# encoding: utf-8
#author: ff0000team


def output_init(name, type, passport):
    file_name = "./reports/" + name + ".html"
    file_object = open(file_name, 'w')
    start_content = '''
<!DOCTYPE html>
<!-- author: e0#ff0000team -->
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>%s - Sreg <Beebeeto></title>
    <link href="./sreg_tmp/app.css" rel="stylesheet">
    <style>
      [ng\:cloak], [ng-cloak], [data-ng-cloak], [x-ng-cloak], .ng-cloak, .x-ng-cloak {
        display: none !important;
      }
      body {
          background-color: #e8e8e8;
          color: #000000;
      }
      header {
        background: #151515;
        border-top: 0px solid #ffc616;
        border-bottom: 3px solid #ffffff;
      }
      a {
        color: #969696;
      }
    </style>
    <script type="text/javascript" src="sreg_tmp/jquery.js"></script>
    <script type="text/javascript">
    window.onload=function(){
        $("#detail").append("   Count: " + $(".website-name").length);
    }
    </script>
  </head>
  <body class="ng-scope" data-feedly-mini="yes">
    <header>
      <div class="container">
        <div class="row">
          <div class="logo">
            <a href="http://buzz.beebeeto.com/" target="_blank">
              <img src="./sreg_tmp/beebeeto_logo.png" alt="beebeeto logo">
            </a>
          </div>
          <h1 class="hidden-xs" style="color: #c62011">>_ Search Registration</h1>
          <h4 style="color: #B51D0F"><p id="detail">%s %s  </p></h4>
          <h2 class="sponsored hidden-xs" style="color: #981C00">Page Generated by <a href="https://buzz.beebeeto.com/" style="color: #c62011">Sreg</a></h2>
        </div>
        <div class="row">
        </div>
      </div>
    </header>
    <section class="">
      <div class="container">
        <div class="row">
          <div ng-show="hasResults" class="col-md-12">
            <table class="table table-hover search-results" id="table">
              <thead>
                <tr>
                  <th class="hidden-xs"><a ng-click="sortResults(&#39;Icon&#39;)">ICON</a></th>
                  <th><a ng-click="sortResults(&#39;Website&#39;)">Website</a></th>
                  <th class="hidden-xs"><a ng-click="sortResults(&#39;Category&#39;)">Category</a></th>
              </tr></thead>
              <tbody>
    ''' % (name, type, passport)
    file_object.write(start_content)
    file_object.close()


def output_finished(name):
    file_name = "./reports/" + name + ".html"
    file_object = open(file_name, 'a')
    end_content = '''
                    </tbody>
                </table>
              </div>
            </div>
          </div>
        </section>
      </body>
    </html>
    '''
    file_object.write(end_content)
    file_object.close()
    print('\n[+] Results the save path: %s' % file_name)


def output_add(category, app_name, website, name, passport_type, icon, description):
    file_name = "./reports/" + passport_type + "_" + name + ".html"
    file_object = open(file_name, 'a')
    mid_content = '''
                        <tr>
                      <td class="hidden-xs owner" bind-once="result.owner">
                        <a href="%s" target="_blank"><img src="%s"></a>
                      </td>
                      <td class="website-name">
                        <h4>
                          <a bind-attr-once="{href: result.website}" bind-once="result.name" href="%s" target="_blank">%s</a>
                        </h4>
                        <p class="description" bind-attr-once="{title: result.description}" bind-once="result.description" title="jQuery Mobile Framework">
                            %s
                        </p>
                      </td>
                      <td class="hidden-xs owner" bind-once="result.owner">%s</td>
                    </tr>
    ''' % (website, icon, website, app_name.encode('utf-8'), description.encode('utf-8'), category.encode('utf-8'))
    file_object.write(mid_content)
    file_object.close()
