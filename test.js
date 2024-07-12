(function () {
    const globalVariables = {
        testName: "Venue Seating Plan - Add Trust Bar",
        pageInitials: "vsp-add-trust-bar",
        testVariation: 1 /* 1, 2, 3 */,
        testVersion: 0.0001,
    };

    function waitForElement(
        waitFor,
        callback,
        minElements = 1,
        isVariable = false,
        timer = 15000,
        frequency = 25
    ) {
        let elements = isVariable
            ? window[waitFor]
            : document.querySelectorAll(waitFor);
        if (timer <= 0) return;
        (!isVariable && elements.length >= minElements) ||
        (isVariable && typeof window[waitFor] !== "undefined")
            ? callback(elements)
            : setTimeout(
                  () =>
                      waitForElement(
                          waitFor,
                          callback,
                          minElements,
                          isVariable,
                          timer - frequency
                      ),
                  frequency
              );
    }

    function addStyleModifier() {
        const styleModifiers = ["sp-body--v1", "sp-body--v2", "sp-body--v3"];
        const targetClass = styleModifiers[globalVariables.testVariation - 1];

        const body = document.querySelector("body");

        // Remove Existing Modifier
        if (body.classList.contains(...styleModifiers)) {
            body.classList.remove(...styleModifiers);
        }

        // Add Modifier
        body.classList.add(targetClass);
    }

    function createLayout() {
        waitForElement(".city-nav", ([targetNode]) => {
            const layout = /* HTML */ `
                <div data-cy="trust-bar" class="trust-bar vsp-trust-bar">
                    <ul data-cy="trust-bar-list" class="trust-bar__list">
                        <li
                            id="seat-views"
                            data-cy="trust-bar-list-item"
                            class="trust-bar__list-item"
                        >
                            <div class="sp-icon-wrapper trust-bar__icon">
                                <span
                                    class="sp-icon sp-icon-photo-camera sp-icon--filled"
                                ></span>
                            </div>
                            <div class="trust-bar__info">
                                <span>225,000+ </span><span>Seat Views</span>
                            </div>
                        </li>
                        <li
                            id="customer-review"
                            data-cy="trust-bar-list-item"
                            class="trust-bar__list-item"
                        >
                            <div class="sp-icon-wrapper trust-bar__icon">
                                <span
                                    class="sp-icon sp-icon-star sp-icon--filled"
                                ></span>
                            </div>
                            <div class="trust-bar__info">
                                <span>Rated Excellent </span
                                ><span>by customers</span>
                            </div>
                        </li>
                        <li
                            id="official-ticket"
                            data-cy="trust-bar-list-item"
                            class="trust-bar__list-item"
                        >
                            <div class="sp-icon-wrapper trust-bar__icon">
                                <span
                                    data-cy="sp-icon"
                                    class="sp-icon sp-icon-security sp-icon--filled"
                                ></span>
                            </div>
                            <div class="trust-bar__info">
                                <span>Official Ticket </span
                                ><span>Guarantee</span>
                            </div>
                        </li>
                    </ul>
                </div>
            `;

            targetNode.insertAdjacentHTML("afterend", layout);
        });
    }

    function clickFunction() {
        const body = document.querySelector("body");
        body.addEventListener("click", (e) => {
            if (e.target.closest("#seat-views.trust-bar__list-item")) {
                console.log("========== seat-views ==========");
            }

            if (e.target.closest("#customer-review.trust-bar__list-item")) {
                console.log("========== customer-reviews ==========");
            }

            if (e.target.closest("#official-ticket.trust-bar__list-item")) {
                console.log("========== official-ticket ==========");
            }
        });
    }

    function appendModal() {
        waitForElement("dfdf", () => {
            const layout = {
                seatViews: `<div class=sp-overlay data-v-4f5834bf=""data-cy=sp-modal-overlay data-v-217132e0=""data-v-23e3c03d=""data-v-2902f3fd=""><div class="sp-modal trust-bar-modal"data-v-217132e0=""><div class="sp-modal-navigation sp-modal-navigation--dark-mode sp-modal-navigation--modal-version trust-bar-modal__navigation"data-v-d8ce10f0=""data-v-23e3c03d=""><div class=sp-modal-navigation__back-wrapper data-v-d8ce10f0=""></div><div class=sp-modal-navigation__close data-v-d8ce10f0=""data-cy=sp-modal-navigation-close><div class=sp-icon-wrapper data-v-d8ce10f0=""><span class="sp-icon sp-icon-close"data-cy=sp-icon style=font-size:22px></span></div></div></div><div class=trust-bar-modal__content data-v-23e3c03d=""><div class=trust-bar-modal-photos data-v-4f5834bf=""><div class=trust-bar-modal-photos__image data-v-4f5834bf=""><img alt=SeatPlan data-v-4f5834bf=""src=/build/images/trust-bar/trust-bar-modal-photos.png></div><div class=trust-bar-modal-photos__info data-v-4f5834bf=""><h2 class="sp-heading sp-heading--primary"data-v-4f5834bf="">225,000 Seat View Photos</h2><p class=sp-paragraph data-v-4f5834bf="">SeatPlan has collected 225,000 view from seat photos from audience members like you. We display photos and prices on interactive seating plans so you can book the best views and avoid the worst!<p class=sp-paragraph data-v-4f5834bf="">We are on a mission to get a photo from every seat. Add photos to earn rewards and help other theatregoers!</p><button class="sp-button sp-button--primary"data-cy=sp-button data-v-4f5834bf=""fdprocessedid=izi7yn type=button>Add Photo</button> <button class="sp-button sp-button--primary sp-button--link"data-cy=sp-button data-v-4f5834bf=""fdprocessedid=0c6chr type=button>Close</button></div></div></div></div></div>`,

                customerReviews: `<div class=sp-overlay data-v-c3d93b06=""data-cy=sp-modal-overlay data-v-217132e0=""data-v-23e3c03d=""data-v-2902f3fd=""><div class="sp-modal trust-bar-modal"data-v-217132e0=""><div class="sp-modal-navigation sp-modal-navigation--modal-version trust-bar-modal__navigation"data-v-d8ce10f0=""data-v-23e3c03d=""><div class=sp-modal-navigation__back-wrapper data-v-d8ce10f0=""></div><div class=sp-modal-navigation__close data-v-d8ce10f0=""data-cy=sp-modal-navigation-close><div class=sp-icon-wrapper data-v-d8ce10f0=""><span class="sp-icon sp-icon-close"data-cy=sp-icon style=font-size:22px></span></div></div></div><div class=trust-bar-modal__content data-v-23e3c03d=""><div class=trust-bar-modal-trustpilot data-v-c3d93b06=""><div class=trust-bar-modal-trustpilot__info data-v-c3d93b06=""><h2 class="sp-heading sp-heading--primary"data-v-c3d93b06="">What Customers Say About SeatPlan</h2><div class=trustpilot-widget data-v-c3d93b06=""data-businessunit-id=5c6844fb9521140001cbf6b0 data-locale=en-GB data-review-languages=en data-style-height=500px data-style-width=100% data-tags=favourite data-template-id=539ad60defb9600b94d7df2c data-theme=light style=position:relative><iframe loading=auto src="https://widget.trustpilot.com/trustboxes/539ad60defb9600b94d7df2c/index.html?businessunitId=5c6844fb9521140001cbf6b0&templateId=539ad60defb9600b94d7df2c#vC3d93b06=&locale=en-GB&reviewLanguages=en&styleHeight=500px&styleWidth=100%25&tags=favourite&theme=light"style=position:relative;height:500px;width:100%;border-style:none;display:block;overflow:hidden title="Customer reviews powered by Trustpilot"></iframe></div><button class="sp-button sp-button--link sp-button--primary"data-cy=sp-button data-v-c3d93b06=""fdprocessedid=mgyk type=button>Close</button></div></div></div></div></div>`,

                officialTicket: `<div class=sp-overlay data-v-771aef57=""data-cy=sp-modal-overlay data-v-217132e0=""data-v-23e3c03d=""data-v-2902f3fd=""><div class="sp-modal trust-bar-modal"data-v-217132e0=""><div class="sp-modal-navigation sp-modal-navigation--modal-version trust-bar-modal__navigation"data-v-d8ce10f0=""data-v-23e3c03d=""><div class=sp-modal-navigation__back-wrapper data-v-d8ce10f0=""></div><div class=sp-modal-navigation__close data-v-d8ce10f0=""data-cy=sp-modal-navigation-close><div class=sp-icon-wrapper data-v-d8ce10f0=""><span class="sp-icon sp-icon-close"data-cy=sp-icon style=font-size:22px></span></div></div></div><div class=trust-bar-modal__content data-v-23e3c03d=""><div class=trust-bar-modal-guarantee data-v-771aef57=""><div class=trust-bar-modal-guarantee__image data-v-771aef57=""><img alt="SeatPlan - Guarantee"data-v-771aef57=""src=/build/images/trust-bar/trust-bar-best-price-guarantee.webp></div><div class=trust-bar-modal-guarantee__info data-v-771aef57=""><h2 class="sp-heading sp-heading--primary"data-v-771aef57="">Offical Ticket Guarantee</h2><p class=sp-paragraph data-v-771aef57="">SeatPlan displays the best prices and ticket deals by aggregating availability and prices from TodayTix USA, Encore Tickets, London Theatre Direct and ATGtickets.<p class=sp-paragraph data-v-771aef57="">All tickets are official, primary tickets direct from venues and show producers. We do not list any secondary market tickets because we don't believe in secondary market rip off pricing.</p><button class="sp-button sp-button--link sp-button--primary"data-cy=sp-button data-v-771aef57=""fdprocessedid=0hz3e9 type=button>Close</button></div></div></div></div></div>`,
            };
        });
    }

    function init() {
        addStyleModifier();
        createLayout();
        clickFunction();
    }

    function pollForExperiment() {
        waitForElement("body.venue-page-wrapper", ([body]) => {
            if (!body.classList.contains(globalVariables.pageInitials)) {
                body.classList.add(globalVariables.pageInitials);
                init();
            }
        });
    }

    pollForExperiment();
})();
